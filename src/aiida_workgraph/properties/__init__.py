from node_graph.utils import get_entries

property_pool = {
    **get_entries(entry_point_name="node_graph.property"),
    **get_entries(entry_point_name="aiida_workgraph.property"),
}