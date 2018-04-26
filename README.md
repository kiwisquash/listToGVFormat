# Introduction

Given a list of strings in input.md, listToMap.py will print the header for a directed graph using the graphviz dot language. 

- Each **non-empty** line is treated as a node for the graph.
- If a line has a colon, then the node name will be assigned based on the text that comes before the first colon in the line. 
- If a line does not have a colon, then the node will be given the name of the form "A" followed by the line number.
- Each line is treated as a label for the node in the graph.
- Line breaks are automatically inserted for the labels because graphviz does not insert line breaks.
    - By default, labels will have no more than 20 characters per line.
    - You can adjust the max number of characters.

# Usage

> `python listToMap.py`

Print the graphviz header with label width capped at 20 characters (default).

> `python listToMap.py 15`

Print the header with label width capped at 15 characters.

> `python listToMap.py 12 > output.gv`

Overwrite the contents of output.gv.

## Sample input

     Level A.1: The beginning of the end of the beginning
     Level B.2: The middle of the end of the middle
     Level C.3: I am the lord of the dance.

     Stage D.a.4: Blah blah blah blah

## Sample output

    digraph map {

     # node [shape = oval, style = filled, fillcolor = white] 
     # edge [color = black,style = solid]
     # attributes can be applied to subgroups of nodes and edges
     # rankdir = 'LR' # Changes direction of graph
     # {rank = same; /\*list of nodes\*/} # rank can also be max, min, source, sink
    
    	A1 [label = "A.1: The beginning\nof the end of the\nbeginning"];
     	B2 [label = "B.2: The middle of\nthe end of the\nmiddle"];
     	C3 [label = "C.3: I am the lord\nof the dance."];
     	Da4 [label = "D.a.4: Blah blah\nblah blah"];
    
    }
