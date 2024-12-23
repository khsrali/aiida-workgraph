from aiida_workgraph.task import Task


class TestAdd(Task):

    identifier: str = "workgraph.test_add"
    name = "TestAAdd"
    node_type = "CALCFUNCTION"
    catalog = "Test"

    _executor = {
        "module": "aiida_workgraph.executors.test",
        "name": "add",
    }

    def create_properties(self) -> None:
        self.properties.new("workgraph.aiida_float", "t", default=1.0)

    def create_sockets(self) -> None:
        self.inputs.clear()
        self.outputs.clear()
        inp = self.inputs.new("workgraph.aiida_float", "x")
        inp.add_property("workgraph.aiida_float", "x", default=0.0)
        inp = self.inputs.new("workgraph.aiida_float", "y")
        inp.add_property("workgraph.aiida_float", "y", default=0.0)
        self.inputs.new("workgraph.any", "_wait", arg_type="none", link_limit=100000)
        self.outputs.new("workgraph.aiida_float", "sum")
        self.outputs.new("workgraph.any", "_wait")
        self.outputs.new("workgraph.any", "_outputs")


class TestSumDiff(Task):

    identifier: str = "workgraph.test_sum_diff"
    name = "TestSumDiff"
    node_type = "CALCFUNCTION"
    catalog = "Test"

    _executor = {
        "module": "aiida_workgraph.executors.test",
        "name": "sum_diff",
    }

    def create_properties(self) -> None:
        self.properties.new("workgraph.aiida_float", "t", default=1.0)

    def create_sockets(self) -> None:
        self.inputs.clear()
        self.outputs.clear()
        inp = self.inputs.new("workgraph.aiida_float", "x")
        inp.add_property("workgraph.aiida_float", "x", default=0.0)
        inp = self.inputs.new("workgraph.aiida_float", "y")
        inp.add_property("workgraph.aiida_float", "y", default=0.0)
        self.inputs.new("workgraph.any", "_wait", arg_type="none", link_limit=100000)
        self.outputs.new("workgraph.aiida_float", "sum")
        self.outputs.new("workgraph.aiida_float", "diff")
        self.outputs.new("workgraph.any", "_wait")
        self.outputs.new("workgraph.any", "_outputs")


class TestArithmeticMultiplyAdd(Task):

    identifier: str = "workgraph.test_arithmetic_multiply_add"
    name = "TestArithmeticMultiplyAdd"
    node_type = "WORKCHAIN"
    catalog = "Test"

    _executor = {
        "name": "core.arithmetic.multiply_add",
        "type": "WorkflowFactory",
    }

    def create_properties(self) -> None:
        pass

    def create_sockets(self) -> None:
        self.inputs.clear()
        self.outputs.clear()
        self.inputs.new("workgraph.any", "code")
        inp = self.inputs.new("workgraph.aiida_int", "x")
        inp.add_property("workgraph.aiida_int", "x", default=0.0)
        inp = self.inputs.new("workgraph.aiida_int", "y")
        inp.add_property("workgraph.aiida_int", "y", default=0.0)
        inp = self.inputs.new("workgraph.aiida_int", "z")
        inp.add_property("workgraph.aiida_int", "z", default=0.0)
        self.inputs.new("workgraph.any", "_wait", arg_type="none", link_limit=100000)
        self.outputs.new("workgraph.aiida_int", "result")
        self.outputs.new("workgraph.any", "_wait")
        self.outputs.new("workgraph.any", "_outputs")
