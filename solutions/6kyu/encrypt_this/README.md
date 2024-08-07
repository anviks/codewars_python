<h2 id="acknowledgments">Acknowledgments:</h2>
<p>I thank <a href="https://www.codewars.com/users/yvonne-liu" data-turbolinks="false" target="_blank">yvonne-liu</a> for the idea and for the example tests :)</p>
<h2 id="description">Description:</h2>
<p>Encrypt this!</p>
<p>You want to create secret messages which can be deciphered by the <a href="https://www.codewars.com/kata/decipher-this" data-turbolinks="false" target="_blank">Decipher this!</a> kata. Here are the conditions:</p>
<ol>
<li>Your message is a string containing space separated words.</li>
<li>You need to encrypt each word in the message using the following rules:<ul>
<li>The first letter must be converted to its ASCII code.</li>
<li>The second letter must be switched with the last letter</li>
</ul>
</li>
<li>Keepin' it simple: There are no special characters in the input.</li>
</ol>
<h2 id="examples">Examples:</h2>
<pre style="display: none;"><code class="language-haskell"><span class="cm-variable">encryptThis</span> <span class="cm-string">"Hello"</span> <span class="cm-builtin">==</span> <span class="cm-string">"72olle"</span>
<span class="cm-variable">encryptThis</span> <span class="cm-string">"good"</span> <span class="cm-builtin">==</span> <span class="cm-string">"103doo"</span>
<span class="cm-variable">encryptThis</span> <span class="cm-string">"hello world"</span> <span class="cm-builtin">==</span> <span class="cm-string">"104olle 119drlo"</span>
</code></pre>
<pre><code class="language-python"><span class="cm-variable">encrypt_this</span>(<span class="cm-string">"Hello"</span>) <span class="cm-operator">==</span> <span class="cm-string">"72olle"</span>
<span class="cm-variable">encrypt_this</span>(<span class="cm-string">"good"</span>) <span class="cm-operator">==</span> <span class="cm-string">"103doo"</span>
<span class="cm-variable">encrypt_this</span>(<span class="cm-string">"hello world"</span>) <span class="cm-operator">==</span> <span class="cm-string">"104olle 119drlo"</span>
</code></pre>
<pre style="display: none;"><code class="language-ruby"><span class="cm-variable">encrypt_this</span>(<span class="cm-string">"Hello"</span>) <span class="cm-operator">==</span> <span class="cm-string">"72olle"</span>
<span class="cm-variable">encrypt_this</span>(<span class="cm-string">"good"</span>) <span class="cm-operator">==</span> <span class="cm-string">"103doo"</span>
<span class="cm-variable">encrypt_this</span>(<span class="cm-string">"hello world"</span>) <span class="cm-operator">==</span> <span class="cm-string">"104olle 119drlo"</span>
</code></pre>
<pre style="display: none;"><code class="language-groovy"><span class="cm-variable">Kata</span>.<span class="cm-property">encryptThis</span>(<span class="cm-string">"Hello"</span>) <span class="cm-operator">==</span> <span class="cm-string">"72olle"</span>
<span class="cm-variable">Kata</span>.<span class="cm-property">encryptThis</span>(<span class="cm-string">"good"</span>) <span class="cm-operator">==</span> <span class="cm-string">"103doo"</span>
<span class="cm-variable">Kata</span>.<span class="cm-property">encryptThis</span>(<span class="cm-string">"hello world"</span>) <span class="cm-operator">==</span> <span class="cm-string">"104olle 119drlo"</span>
</code></pre>
<pre style="display: none;"><code class="language-scala"><span class="cm-variable">Encrypt</span>.<span class="cm-variable">encryptThis</span>(<span class="cm-string">"Hello"</span>) <span class="cm-operator">==</span> <span class="cm-string">"72olle"</span>
<span class="cm-variable">Encrypt</span>.<span class="cm-variable">encryptThis</span>(<span class="cm-string">"good"</span>) <span class="cm-operator">==</span> <span class="cm-string">"103doo"</span>
<span class="cm-variable">Encrypt</span>.<span class="cm-variable">encryptThis</span>(<span class="cm-string">"hello world"</span>) <span class="cm-operator">==</span> <span class="cm-string">"104olle 119drlo"</span>
</code></pre>
<pre style="display: none;"><code class="language-java"><span class="cm-variable">Kata</span>.<span class="cm-variable">encryptThis</span>(<span class="cm-string">"Hello"</span>) <span class="cm-operator">=&gt;</span> <span class="cm-string">"72olle"</span>
<span class="cm-variable">Kata</span>.<span class="cm-variable">encryptThis</span>(<span class="cm-string">"good"</span>) <span class="cm-operator">=&gt;</span> <span class="cm-string">"103doo"</span>
<span class="cm-variable">Kata</span>.<span class="cm-variable">encryptThis</span>(<span class="cm-string">"hello world"</span>) <span class="cm-operator">=&gt;</span> <span class="cm-string">"104olle 119drlo"</span>
</code></pre>
<pre style="display: none;"><code class="language-javascript"><span class="cm-variable">encryptThis</span>(<span class="cm-string">"Hello"</span>) <span class="cm-operator">===</span> <span class="cm-string">"72olle"</span>
<span class="cm-variable">encryptThis</span>(<span class="cm-string">"good"</span>) <span class="cm-operator">===</span> <span class="cm-string">"103doo"</span>
<span class="cm-variable">encryptThis</span>(<span class="cm-string">"hello world"</span>) <span class="cm-operator">===</span> <span class="cm-string">"104olle 119drlo"</span>
</code></pre>
<pre style="display: none;"><code class="language-coffeescript"><span class="cm-variable">encryptThis</span><span class="cm-punctuation">(</span><span class="cm-string">"Hello"</span><span class="cm-punctuation">)</span> <span class="cm-operator">==</span><span class="cm-punctuation">=</span> <span class="cm-string">"72olle"</span>
<span class="cm-variable">encryptThis</span><span class="cm-punctuation">(</span><span class="cm-string">"good"</span><span class="cm-punctuation">)</span> <span class="cm-operator">==</span><span class="cm-punctuation">=</span> <span class="cm-string">"103doo"</span>
<span class="cm-variable">encryptThis</span><span class="cm-punctuation">(</span><span class="cm-string">"hello world"</span><span class="cm-punctuation">)</span> <span class="cm-operator">==</span><span class="cm-punctuation">=</span> <span class="cm-string">"104olle 119drlo"</span>
</code></pre>
<pre style="display: none;"><code class="language-c"><span class="cm-variable">encrypt_this</span>(<span class="cm-string">"Hello"</span>) <span class="cm-operator">==</span> <span class="cm-string">"72olle"</span>
<span class="cm-variable">encrypt_this</span>(<span class="cm-string">"good"</span>) <span class="cm-operator">==</span> <span class="cm-string">"103doo"</span>
<span class="cm-variable">encrypt_this</span>(<span class="cm-string">"hello world"</span>) <span class="cm-operator">==</span> <span class="cm-string">"104olle 119drlo"</span>
</code></pre>
<pre style="display: none;"><code class="language-cpp"><span class="cm-variable">encrypt_this</span>(<span class="cm-string">"Hello"</span>) <span class="cm-operator">==</span> <span class="cm-string">"72olle"</span>
<span class="cm-variable">encrypt_this</span>(<span class="cm-string">"good"</span>) <span class="cm-operator">==</span> <span class="cm-string">"103doo"</span>
<span class="cm-variable">encrypt_this</span>(<span class="cm-string">"hello world"</span>) <span class="cm-operator">==</span> <span class="cm-string">"104olle 119drlo"</span>
</code></pre>
<pre style="display: none;"><code class="language-go"><span class="cm-variable">EncryptThis</span>(<span class="cm-string">"Hello"</span>) <span class="cm-operator">==</span> <span class="cm-string">"72olle"</span>
<span class="cm-variable">EncryptThis</span>(<span class="cm-string">"good"</span>) <span class="cm-operator">==</span> <span class="cm-string">"103doo"</span>
<span class="cm-variable">EncryptThis</span>(<span class="cm-string">"hello world"</span>) <span class="cm-operator">==</span> <span class="cm-string">"104olle 119drlo"</span>
</code></pre>
<pre style="display: none;"><code class="language-csharp"><span class="cm-variable">Kata</span>.<span class="cm-variable">EncryptThis</span>(<span class="cm-string">"Hello"</span>) <span class="cm-operator">==</span> <span class="cm-string">"72olle"</span>
<span class="cm-variable">Kata</span>.<span class="cm-variable">EncryptThis</span>(<span class="cm-string">"good"</span>) <span class="cm-operator">==</span> <span class="cm-string">"103doo"</span>
<span class="cm-variable">Kata</span>.<span class="cm-variable">EncryptThis</span>(<span class="cm-string">"hello world"</span>) <span class="cm-operator">==</span> <span class="cm-string">"104olle 119drlo"</span>
</code></pre>
<pre style="display: none;"><code class="language-vb"><span class="cm-variable">Kata</span><span class="cm-variable">.EncryptThis</span>(<span class="cm-string">"Hello"</span>) = <span class="cm-string">"72olle"</span>
<span class="cm-variable">Kata</span><span class="cm-variable">.EncryptThis</span>(<span class="cm-string">"good"</span>) = <span class="cm-string">"103doo"</span>
<span class="cm-variable">Kata</span><span class="cm-variable">.EncryptThis</span>(<span class="cm-string">"hello world"</span>) = <span class="cm-string">"104olle 119drlo"</span>
</code></pre>
<pre style="display: none;"><code class="language-clojure"><span class="cm-bracket">(</span><span class="cm-keyword">=</span> <span class="cm-bracket">(</span><span class="cm-builtin">encrypt-this</span> <span class="cm-string">"Hello"</span><span class="cm-bracket">)</span> <span class="cm-string">"72olle"</span><span class="cm-bracket">)</span>
<span class="cm-bracket">(</span><span class="cm-keyword">=</span> <span class="cm-bracket">(</span><span class="cm-builtin">encrypt-this</span> <span class="cm-string">"good"</span> <span class="cm-bracket">)</span> <span class="cm-string">"103doo"</span><span class="cm-bracket">)</span>
<span class="cm-bracket">(</span><span class="cm-keyword">=</span> <span class="cm-bracket">(</span><span class="cm-builtin">encrypt-this</span> <span class="cm-string">"hello world"</span><span class="cm-bracket">)</span> <span class="cm-string">"104olle 119drlo"</span><span class="cm-bracket">)</span>
</code></pre>
<pre style="display: none;"><code class="language-rust"><span class="cm-variable">encrypt_this</span>(<span class="cm-string">"</span><span class="cm-string">Hello</span><span class="cm-string">"</span>) <span class="cm-operator">==</span> <span class="cm-string">"</span><span class="cm-string">72olle</span><span class="cm-string">"</span>
<span class="cm-variable">encrypt_this</span>(<span class="cm-string">"</span><span class="cm-string">good</span><span class="cm-string">"</span>) <span class="cm-operator">==</span> <span class="cm-string">"</span><span class="cm-string">103doo</span><span class="cm-string">"</span>
<span class="cm-variable">encrypt_this</span>(<span class="cm-string">"</span><span class="cm-string">hello world</span><span class="cm-string">"</span>) <span class="cm-operator">==</span> <span class="cm-string">"</span><span class="cm-string">104olle 119drlo</span><span class="cm-string">"</span>
</code></pre>
<pre style="display: none;"><code class="language-lua"><span class="cm-variable">solution.encrypt_this</span>(<span class="cm-string">"Hello"</span>) == <span class="cm-string">"72olle"</span>
<span class="cm-variable">solution.encrypt_this</span>(<span class="cm-string">"good"</span>) == <span class="cm-string">"103doo"</span>
<span class="cm-variable">solution.encrypt_this</span>(<span class="cm-string">"hello world"</span>) == <span class="cm-string">"104olle 119drlo"</span>
</code></pre>
<pre style="display: none;"><code class="language-php"><span class="cm-variable">encryptThis</span>(<span class="cm-string">"</span><span class="cm-string">Hello"</span>) <span class="cm-operator">===</span> <span class="cm-string">"</span><span class="cm-string">72olle"</span>
<span class="cm-variable">encryptThis</span>(<span class="cm-string">"</span><span class="cm-string">good"</span>) <span class="cm-operator">===</span> <span class="cm-string">"</span><span class="cm-string">103doo"</span>
<span class="cm-variable">encryptThis</span>(<span class="cm-string">"</span><span class="cm-string">hello world"</span>) <span class="cm-operator">===</span> <span class="cm-string">"</span><span class="cm-string">104olle 119drlo"</span>
</code></pre>
