from core.viz.table import table_generator
from core.viz.network import network_generator


def table_example():
    cols = ['name', 'age', 'sex']

    rows = [
        ['john', 12, 'M'],
        ['doe', '15', 'F'],
        ['foo', '17', 'M']
    ]

    table_str = table_generator.generate_table_html('table_example', cols, rows,
                                                    css_classes=[
                                                        "table",
                                                        "table-striped",
                                                        "table-bordered",
                                                        "table-sm"
                                                    ])

    table_generator.add_table_to_template('table_example', table_str)


def digraph_example():
    nodes = [
        {
            'id': '1',
            'label': 'a'
        },
        {
            'id': '2',
            'label': 'b'
        },
        {
            'id': '3',
            'label': 'c'
        }
    ]

    edges = [
        {
            'from': '1',
            'to': '2',
            'arrows': 'to'
        },
        {
            'from': '2',
            'to': '3',
            'color': {
                'color': 'red'
            },
            'arrows': 'to'
        },
        {
            'from': '3',
            'to': '1',
            'dashes': True,
            'arrows': 'to'
        }
    ]

    nodes_str, edges_str = network_generator.generate_network_html('digraph_example',
                                                                   nodes, edges)

    network_generator.add_network_to_template('digraph_example', nodes_str, edges_str)
