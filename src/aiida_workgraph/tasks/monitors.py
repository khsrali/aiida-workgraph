from aiida_workgraph.task import Task


class TimeMonitor(Task):
    """Monitor the time"""

    identifier = "workgraph.time_monitor"
    name = "TimeMonitor"
    node_type = "MONITOR"
    catalog = "Monitor"

    _executor = {
        "module": "aiida_workgraph.executors.monitors",
        "name": "time_monitor",
    }

    def create_sockets(self) -> None:
        self.inputs.clear()
        self.outputs.clear()
        self.inputs.new("workgraph.any", "time")
        inp = self.inputs.new("workgraph.any", "interval")
        inp.add_property("workgraph.any", default=1.0)
        inp = self.inputs.new("workgraph.any", "timeout")
        inp.add_property("workgraph.any", default=86400.0)
        self.inputs.new("workgraph.any", "_wait", arg_type="none", link_limit=100000)
        inp.link_limit = 100000
        self.outputs.new("workgraph.any", "result")
        self.outputs.new("workgraph.any", "_wait")


class FileMonitor(Task):
    """Monitor the file"""

    identifier = "workgraph.file_monitor"
    name = "FileMonitor"
    node_type = "MONITOR"
    catalog = "Monitor"

    _executor = {
        "module": "aiida_workgraph.executors.monitors",
        "name": "file_monitor",
    }

    def create_sockets(self) -> None:
        self.inputs.clear()
        self.outputs.clear()
        self.inputs.new("workgraph.any", "filepath")
        inp = self.inputs.new("workgraph.any", "interval")
        inp.add_property("workgraph.any", default=1.0)
        inp = self.inputs.new("workgraph.any", "timeout")
        inp.add_property("workgraph.any", default=86400.0)
        self.inputs.new("workgraph.any", "_wait", arg_type="none", link_limit=100000)
        inp.link_limit = 100000
        self.outputs.new("workgraph.any", "result")
        self.outputs.new("workgraph.any", "_wait")


class TaskMonitor(Task):
    """Monitor the file"""

    identifier = "workgraph.task_monitor"
    name = "TaskMonitor"
    node_type = "MONITOR"
    catalog = "Monitor"

    _executor = {
        "module": "aiida_workgraph.executors.monitors",
        "name": "task_monitor",
    }

    def create_sockets(self) -> None:
        self.inputs.clear()
        self.outputs.clear()
        self.inputs.new("workgraph.any", "workgraph_pk")
        self.inputs.new("workgraph.any", "workgraph_name")
        self.inputs.new("workgraph.any", "task_name")
        inp = self.inputs.new("workgraph.any", "interval")
        inp.add_property("workgraph.any", default=1.0)
        inp = self.inputs.new("workgraph.any", "timeout")
        inp.add_property("workgraph.any", default=86400.0)
        self.inputs.new("workgraph.any", "_wait", arg_type="none", link_limit=100000)
        inp.link_limit = 100000
        self.outputs.new("workgraph.any", "result")
        self.outputs.new("workgraph.any", "_wait")
