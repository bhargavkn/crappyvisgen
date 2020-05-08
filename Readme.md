### What is this?

Just something I use personally to generate one time static visualizations

### Usage

Creating visualizations:

Add required sections in `index.html` file and write code inside the `useme` directory 
that will generate data and use the functionalities provided in core to generated the 
visulizations.


### Examples:

#### Table

Consider that you want to add a table to your html page. 
For this, you'll first add a placeholder `div` with the 
type `table` and give it a unique `id` for the table to be 
rendered in the html page. You will also declare a placeholder 
variable within the div that the tool will use to substitute the
required html.

```html
.
.
.
<body>
    <div type="table" id="table_example">
        $table_example
    </div>
</body>
.
.
.
```

Then, you can go ahead and view the technique used to fill in data
into this div in the `useme.examples` files's `table_example()` method. 


#### Directed Graph

You'll add a placeholder `div` with the type `network` and give it a unique `id`
for the digraph to be rendered in the html page. You will also declare a placeholder
within the div like before.

```html
.
.
.
<body>
    <div type="network" id="digraph_example">
        $digraph_example
    </div>
</body>
.
.
.
```

View the example in `useme.examples` file's `digraph_example()` method.