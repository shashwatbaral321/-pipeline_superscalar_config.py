#pipeline_superscalar_config.py
# Defining the different pipeline stages

class FetchStage:
    def __init__(self):
        self.instruction = None

    def fetch(self, instruction):
        self.instruction = instruction
        print(f"Fetching instruction: {instruction}")
        return self.instruction


class DecodeStage:
    def __init__(self):
        self.decoded_instruction = None

    def decode(self, instruction):
        self.decoded_instruction = f"Decoded({instruction})"
        print(f"Decoding instruction: {instruction}")
        return self.decoded_instruction


class ExecuteStage:
    def __init__(self):
        self.result = None

    def execute(self, decoded_instruction):
        self.result = f"Executed({decoded_instruction})"
        print(f"Executing instruction: {decoded_instruction}")
        return self.result


class MemoryStage:
    def __init__(self):
        self.memory_access = None

    def access_memory(self, result):
        self.memory_access = f"Memory({result})"
        print(f"Memory access for: {result}")
        return self.memory_access


class WritebackStage:
    def __init__(self):
        self.writeback_result = None

    def writeback(self, memory_access):
        self.writeback_result = f"Writeback({memory_access})"
        print(f"Writing back result: {memory_access}")
        return self.writeback_result


# Superscalar Pipeline Class
class SuperscalarPipeline:
    def __init__(self, issue_width=2):
        self.issue_width = issue_width
        self.fetch_stage = FetchStage()
        self.decode_stage = DecodeStage()
        self.execute_stage = ExecuteStage()
        self.memory_stage = MemoryStage()
        self.writeback_stage = WritebackStage()
        self.instruction_queue = []
        self.total_cycles = 0
        self.instructions_completed = 0

    def run_pipeline(self, instructions):
        for instruction in instructions:
            self.instruction_queue.append(instruction)
            if len(self.instruction_queue) >= self.issue_width:
                self.issue_instructions()

        # Complete any remaining instructions
        while self.instruction_queue:
            self.issue_instructions()

    def issue_instructions(self):
        issued_instructions = self.instruction_queue[:self.issue_width]
        self.instruction_queue = self.instruction_queue[self.issue_width:]

        for instruction in issued_instructions:
            self.total_cycles += 1
            fetched = self.fetch_stage.fetch(instruction)
            decoded = self.decode_stage.decode(fetched)
            executed = self.execute_stage.execute(decoded)
            memory_access = self.memory_stage.access_memory(executed)
            self.writeback_stage.writeback(memory_access)
            self.instructions_completed += 1
            print(f"Instruction {instruction} issued and completed")

        print(f"Issued {len(issued_instructions)} instructions in this cycle")


# Example usage of SuperscalarPipeline
instructions = [
    "ADD r1, r2, r3",
    "SUB r4, r5, r6",
    "MUL r7, r8, r9",
    "DIV r10, r11, r12"
]

# Create and run the pipeline with an issue width of 2
pipeline = SuperscalarPipeline(issue_width=2)
pipeline.run_pipeline(instructions)
