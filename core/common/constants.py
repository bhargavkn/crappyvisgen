import re

template_filename = "index.html.tpl"
workdir_dirname = ".workdir"
temporary_template_filename = "index.temp.html"
temporary_template_filepath = workdir_dirname + "/" + temporary_template_filename
output_filename = "index.html"

########### JS Script Constants ###########

# Table
datatable_declaration_js_script_tpl = "\tdataTable_{0} = new DataTable(\"#{0}\");\n"

# Network
network_js_script_tpl = """

    // {0} network begin
    var {0}_container = document.getElementById('{0}');
    var {0}_nodes = new vis.DataSet(${0}_graph_nodes);
    var {0}_edges = new vis.DataSet(${0}_graph_edges);
    var {0}_data = {{
        nodes: {0}_nodes,
        edges: {0}_edges
    }};
    var {0}_options = {{}};
    var {0}_network = new vis.Network(
        {0}_container, 
        {0}_data, 
        {0}_options
    );
    // {0} network end
    
"""
network_js_nodes_var_template_placeholder = "{}_graph_nodes"  # line 18
network_js_edges_var_template_placeholder = "{}_graph_edges"  # line 19

## REs
table_div_matcher_re = re.compile(r'.*div type=[\"\']table[\"\'].*')
network_div_matcher_re = re.compile(r'.*div type=[\"\']network[\"\'].*')
html_id_matcher_re = re.compile(r'id=[\'\"][a-zA-Z_]+[\"\']')
