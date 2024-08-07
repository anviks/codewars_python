<p>If you finish this kata, you can try <a href="http://www.codewars.com/kata/insane-coloured-triangles" data-turbolinks="false" target="_blank">Insane Coloured Triangles</a> by Bubbler, which is a <em><strong>much</strong></em> harder version of this one.</p>
<p>A coloured triangle is created from a row of colours, each of which is red, green or blue. Successive rows, each containing one fewer colour than the last, are generated by considering the two touching colours in the previous row. If these colours are identical, the same colour is used in the new row. If they are different, the missing colour is used in the new row. This is continued until the final row, with only a single colour, is generated.</p>
<p>The different possibilities are:</p>
<pre><code>Colour here:        G G        B G        R G        B R
Becomes colour:      G          R          B          G
</code></pre>
<p>With a bigger example:</p>
<pre><code>R R G B R G B B
 R B R G B R B
  G G B R G G
   G R G B G
    B B R R
     B G R
      R B
       G
</code></pre>
<p>You will be given the first row of the triangle as a string and its your job to return the final colour which would appear in the bottom row as a string. In the case of the example above, you would the given <code>RRGBRGBB</code> you should return <code>G</code>.</p>
<ul>
<li>The input string will only contain the uppercase letters <code>R, G, B</code> and there will be at least one letter so you do not have to test for invalid input.</li>
<li>If you are only given one colour as the input, return that colour.</li>
</ul>
<p><em>Adapted from the 2017 British Informatics Olympiad</em></p>
