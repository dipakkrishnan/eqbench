from src.ollama_client import generate_completion
from src.embeddings import generate_embeddings
from src.extractor import Extractor
from src.graph import CoTGraph
from src.semantic_similarity import cosine_similarity
from src.logger import logger

MAX_GRAPH_SIZE = 5
NODE_PREFIX = "thought_{index}"


class Model:

    def __init__(self):
        self.thought_graph = CoTGraph()

    def forward(self, prompt: str):
        # extract reasoning from completion
        completion = generate_completion(prompt)
        extractor = Extractor(completion)
        reasoning = extractor.extract_reasoning()
        answer = extractor.extract_answer()
        reasoning_steps = extractor.split_reasoning_steps(reasoning)

        logger.info("Generated completion and parsed reasoning steps.")

        # add to thought graph
        for i in range(len(reasoning_steps[:MAX_GRAPH_SIZE])):
            thought = reasoning_steps[i]
            self.thought_graph.add_node(
                NODE_PREFIX.format(index=i),
                reasoning=thought,
                embedding=generate_embeddings(thought),
            )
            logger.info(f"Added {NODE_PREFIX.format(index=i)} to thought graph.")

        # connect edges
        for i in range(1, MAX_GRAPH_SIZE):
            prev_node = NODE_PREFIX.format(index=i - 1)
            current_node = NODE_PREFIX.format(index=i)
            weight = cosine_similarity(
                self.thought_graph.graph.nodes[prev_node]["embedding"],
                self.thought_graph.graph.nodes[current_node]["embedding"]
            )
            self.thought_graph.add_edge(
                prev_node,
                current_node,
                weight=weight,
            )
            self.logger.info(f"Added edge between {prev_node} and {current_node} with weight={weight}.")

        # visualize
        self.thought_graph.visualize()

        print(self.thought_graph)


if __name__ == "__main__":
    m = Model()
    m.forward("how should i think about multiplication?")
