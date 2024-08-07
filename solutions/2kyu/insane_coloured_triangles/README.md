<h1 id="disclaimer">Disclaimer</h1>
<p>This Kata is an insane step-up from <a href="https://www.codewars.com/kata/coloured-triangles" data-turbolinks="false" target="_blank">Avanta's Kata</a>,
so I recommend to solve it first before trying this one.</p>
<h1 id="problem-description">Problem Description</h1>
<p>A coloured triangle is created from a row of colours, each of which is red, green or blue. Successive rows, each containing one fewer colour than the last, are generated by considering the two touching colours in the previous row. If these colours are identical, the same colour is used in the new row. If they are different, the missing colour is used in the new row. This is continued until the final row, with only a single colour, is generated.</p>
<p>For example, different possibilities are:</p>
<pre><code>Colour here:            G G        B G        R G        B R
Becomes colour here:     G          R          B          G
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
<p>You will be given the first row of the triangle as a string and its your job to return the final colour which would appear in the bottom row as a string. In the case of the example above, you would be given 'RRGBRGBB', and you should return 'G'.</p>
<h1 id="constraints">Constraints</h1>
<p><code>1 &lt;= length(row) &lt;= 10 ** 5</code></p>
<p>The input string will only contain the uppercase letters 'B', 'G' or 'R'.</p>
<p>The exact number of test cases will be as follows:</p>
<ul>
<li><code>100</code> tests of <code>100 &lt;= length(row) &lt;= 1000</code></li>
<li><code>100</code> tests of <code>1000 &lt;= length(row) &lt;= 10000</code></li>
<li><code>100</code> tests of <code>10000 &lt;= length(row) &lt;= 100000</code></li>
</ul>
<h1 id="examples">Examples</h1>
<pre style="display: none;"><code class="language-javascript"><span class="cm-variable">triangle</span>(<span class="cm-string">'B'</span>) <span class="cm-operator">==</span> <span class="cm-string">'B'</span>
<span class="cm-variable">triangle</span>(<span class="cm-string">'GB'</span>) <span class="cm-operator">==</span> <span class="cm-string">'R'</span>
<span class="cm-variable">triangle</span>(<span class="cm-string">'RRR'</span>) <span class="cm-operator">==</span> <span class="cm-string">'R'</span>
<span class="cm-variable">triangle</span>(<span class="cm-string">'RGBG'</span>) <span class="cm-operator">==</span> <span class="cm-string">'B'</span>
<span class="cm-variable">triangle</span>(<span class="cm-string">'RBRGBRB'</span>) <span class="cm-operator">==</span> <span class="cm-string">'G'</span>
<span class="cm-variable">triangle</span>(<span class="cm-string">'RBRGBRBGGRRRBGBBBGG'</span>) <span class="cm-operator">==</span> <span class="cm-string">'G'</span>
</code></pre>
<pre><code class="language-python"><span class="cm-variable">triangle</span>(<span class="cm-string">'B'</span>) <span class="cm-operator">==</span> <span class="cm-string">'B'</span>
<span class="cm-variable">triangle</span>(<span class="cm-string">'GB'</span>) <span class="cm-operator">==</span> <span class="cm-string">'R'</span>
<span class="cm-variable">triangle</span>(<span class="cm-string">'RRR'</span>) <span class="cm-operator">==</span> <span class="cm-string">'R'</span>
<span class="cm-variable">triangle</span>(<span class="cm-string">'RGBG'</span>) <span class="cm-operator">==</span> <span class="cm-string">'B'</span>
<span class="cm-variable">triangle</span>(<span class="cm-string">'RBRGBRB'</span>) <span class="cm-operator">==</span> <span class="cm-string">'G'</span>
<span class="cm-variable">triangle</span>(<span class="cm-string">'RBRGBRBGGRRRBGBBBGG'</span>) <span class="cm-operator">==</span> <span class="cm-string">'G'</span>
</code></pre>
<pre style="display: none;"><code class="language-ruby"><span class="cm-variable">triangle</span>(<span class="cm-string">'B'</span>) <span class="cm-operator">==</span> <span class="cm-string">'B'</span>
<span class="cm-variable">triangle</span>(<span class="cm-string">'GB'</span>) <span class="cm-operator">==</span> <span class="cm-string">'R'</span>
<span class="cm-variable">triangle</span>(<span class="cm-string">'RRR'</span>) <span class="cm-operator">==</span> <span class="cm-string">'R'</span>
<span class="cm-variable">triangle</span>(<span class="cm-string">'RGBG'</span>) <span class="cm-operator">==</span> <span class="cm-string">'B'</span>
<span class="cm-variable">triangle</span>(<span class="cm-string">'RBRGBRB'</span>) <span class="cm-operator">==</span> <span class="cm-string">'G'</span>
<span class="cm-variable">triangle</span>(<span class="cm-string">'RBRGBRBGGRRRBGBBBGG'</span>) <span class="cm-operator">==</span> <span class="cm-string">'G'</span>
</code></pre>
<pre style="display: none;"><code class="language-java"><span class="cm-variable">Kata</span>.<span class="cm-variable">triangle</span>(<span class="cm-string">"B"</span>) <span class="cm-operator">==</span> <span class="cm-string">'B'</span>
<span class="cm-variable">Kata</span>.<span class="cm-variable">triangle</span>(<span class="cm-string">"GB"</span>) <span class="cm-operator">==</span> <span class="cm-string">'R'</span>
<span class="cm-variable">Kata</span>.<span class="cm-variable">triangle</span>(<span class="cm-string">"RRR"</span>) <span class="cm-operator">==</span> <span class="cm-string">'R'</span>
<span class="cm-variable">Kata</span>.<span class="cm-variable">triangle</span>(<span class="cm-string">"RGBG"</span>) <span class="cm-operator">==</span> <span class="cm-string">'B'</span>
<span class="cm-variable">Kata</span>.<span class="cm-variable">triangle</span>(<span class="cm-string">"RBRGBRB"</span>) <span class="cm-operator">==</span> <span class="cm-string">'G'</span>
<span class="cm-variable">Kata</span>.<span class="cm-variable">triangle</span>(<span class="cm-string">"RBRGBRBGGRRRBGBBBGG"</span>) <span class="cm-operator">==</span> <span class="cm-string">'G'</span>
</code></pre>
<pre style="display: none;"><code class="language-cpp"><span class="cm-variable">triangle</span>(<span class="cm-string">"B"</span>) <span class="cm-operator">==</span> <span class="cm-string">'B'</span>;
<span class="cm-variable">triangle</span>(<span class="cm-string">"GB"</span>) <span class="cm-operator">==</span> <span class="cm-string">'R'</span>;
<span class="cm-variable">triangle</span>(<span class="cm-string">"RRR"</span>) <span class="cm-operator">==</span> <span class="cm-string">'R'</span>;
<span class="cm-variable">triangle</span>(<span class="cm-string">"RGBG"</span>) <span class="cm-operator">==</span> <span class="cm-string">'B'</span>;
<span class="cm-variable">triangle</span>(<span class="cm-string">"RBRGBRB"</span>) <span class="cm-operator">==</span> <span class="cm-string">'G'</span>;
<span class="cm-variable">triangle</span>(<span class="cm-string">"RBRGBRBGGRRRBGBBBGG"</span>) <span class="cm-operator">==</span> <span class="cm-string">'G'</span>;
</code></pre>
<pre style="display: none;"><code class="language-haskell"><span class="cm-comment">-- Input will actually be `Vector Char` instead of `[Char]`. You'll need the access speed.</span>

<span class="cm-variable">triangle</span> <span class="cm-string">"B"</span> <span class="cm-builtin">==</span> <span class="cm-string">'B'</span>
<span class="cm-variable">triangle</span> <span class="cm-string">"GB"</span> <span class="cm-builtin">==</span> <span class="cm-string">'R'</span>
<span class="cm-variable">triangle</span> <span class="cm-string">"RRR"</span> <span class="cm-builtin">==</span> <span class="cm-string">'R'</span>
<span class="cm-variable">triangle</span> <span class="cm-string">"RGBG"</span> <span class="cm-builtin">==</span> <span class="cm-string">'B'</span>
<span class="cm-variable">triangle</span> <span class="cm-string">"RBRGBRB"</span> <span class="cm-builtin">==</span> <span class="cm-string">'G'</span>
<span class="cm-variable">triangle</span> <span class="cm-string">"RBRGBRBGGRRRBGBBBGG"</span> <span class="cm-builtin">==</span> <span class="cm-string">'G'</span>
</code></pre>
<pre style="display: none;"><code class="language-elixir"><span class="cm-tag">Kata</span><span class="cm-operator">.</span><span class="cm-property">triangle</span>(<span class="cm-string">"B"</span>) <span class="cm-operator">=</span><span class="cm-operator">=</span> <span class="cm-string">"B"</span>
<span class="cm-tag">Kata</span><span class="cm-operator">.</span><span class="cm-property">triangle</span>(<span class="cm-string">"GB"</span>) <span class="cm-operator">=</span><span class="cm-operator">=</span> <span class="cm-string">"R"</span>
<span class="cm-tag">Kata</span><span class="cm-operator">.</span><span class="cm-property">triangle</span>(<span class="cm-string">"RRR"</span>) <span class="cm-operator">=</span><span class="cm-operator">=</span> <span class="cm-string">"R"</span>
<span class="cm-tag">Kata</span><span class="cm-operator">.</span><span class="cm-property">triangle</span>(<span class="cm-string">"RGBG"</span>) <span class="cm-operator">=</span><span class="cm-operator">=</span> <span class="cm-string">"B"</span>
<span class="cm-tag">Kata</span><span class="cm-operator">.</span><span class="cm-property">triangle</span>(<span class="cm-string">"RBRGBRB"</span>) <span class="cm-operator">=</span><span class="cm-operator">=</span> <span class="cm-string">"G"</span>
<span class="cm-tag">Kata</span><span class="cm-operator">.</span><span class="cm-property">triangle</span>(<span class="cm-string">"RBRGBRBGGRRRBGBBBGG"</span>) <span class="cm-operator">=</span><span class="cm-operator">=</span> <span class="cm-string">"G"</span>
</code></pre>
<pre style="display: none;"><code class="language-commonlisp"><span class="cm-bracket">(</span><span class="cm-variable">equal</span> <span class="cm-bracket">(</span><span class="cm-variable">triangle</span> <span class="cm-string">"B"</span><span class="cm-bracket">)</span> <span class="cm-string-2">#\B</span><span class="cm-bracket">)</span>
<span class="cm-bracket">(</span><span class="cm-variable">equal</span> <span class="cm-bracket">(</span><span class="cm-variable">triangle</span> <span class="cm-string">"GB"</span><span class="cm-bracket">)</span> <span class="cm-string-2">#\R</span><span class="cm-bracket">)</span>
<span class="cm-bracket">(</span><span class="cm-variable">equal</span> <span class="cm-bracket">(</span><span class="cm-variable">triangle</span> <span class="cm-string">"RRR"</span><span class="cm-bracket">)</span> <span class="cm-string-2">#\R</span><span class="cm-bracket">)</span>
<span class="cm-bracket">(</span><span class="cm-variable">equal</span> <span class="cm-bracket">(</span><span class="cm-variable">triangle</span> <span class="cm-string">"RGBG"</span><span class="cm-bracket">)</span> <span class="cm-string-2">#\B</span><span class="cm-bracket">)</span>
<span class="cm-bracket">(</span><span class="cm-variable">equal</span> <span class="cm-bracket">(</span><span class="cm-variable">triangle</span> <span class="cm-string">"RBRGBRB"</span><span class="cm-bracket">)</span> <span class="cm-string-2">#\G</span><span class="cm-bracket">)</span>
<span class="cm-bracket">(</span><span class="cm-variable">equal</span> <span class="cm-bracket">(</span><span class="cm-variable">triangle</span> <span class="cm-string">"RBRGBRBGGRRRBGBBBGG"</span><span class="cm-bracket">)</span> <span class="cm-string-2">#\G</span><span class="cm-bracket">)</span>
</code></pre>
