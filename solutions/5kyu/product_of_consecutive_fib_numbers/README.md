<p>The Fibonacci numbers are the numbers in the following integer sequence (Fn):</p>
<blockquote>
<p>0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...</p>
</blockquote>
<p>such as </p>
<blockquote>
<p>F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.</p>
</blockquote>
<p>Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying </p>
<blockquote>
<p>F(n) * F(n+1) = prod.</p>
</blockquote>
<p>Your function productFib takes an integer (prod) and returns
an array: </p>
<pre><code>[F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
</code></pre>
<p>depending on the language if F(n) * F(n+1) = prod.</p>
<p>If you don't find two consecutive F(n) verifying <code>F(n) * F(n+1) = prod</code>you will return</p>
<pre><code>[F(n), F(n+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
</code></pre>
<p>F(n) being the smallest one such as <code>F(n) * F(n+1) &gt; prod</code>.</p>
<h4 id="some-examples-of-return">Some Examples of Return:</h4>
<p>(depend on the language)</p>
<pre><code>productFib(714) # should return (21, 34, true), 
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

productFib(800) # should return (34, 55, false), 
                # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 &lt; 800 &lt; 34 * 55
-----
productFib(714) # should return [21, 34, true], 
productFib(800) # should return [34, 55, false], 
-----
productFib(714) # should return {21, 34, 1}, 
productFib(800) # should return {34, 55, 0},        
-----
productFib(714) # should return {21, 34, true}, 
productFib(800) # should return {34, 55, false}, 
</code></pre>
<h4 id="note">Note:</h4>
<ul>
<li>You can see examples for your language in "Sample Tests".</li>
</ul>
