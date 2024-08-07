<p>Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings. Consonants are any letters of the alphabet except <code>"aeiou"</code>. </p>
<p>We shall assign the following values: <code>a = 1, b = 2, c = 3, .... z = 26</code>.</p>
<p>For example, for the word "zodiacs", let's cross out the vowels. We get: "z <strong><del>o</del></strong> d <strong><del>ia</del></strong> cs"</p>
<pre><code class="language-haskell"><span class="cm-comment">-- The consonant substrings are: "z", "d" and "cs" and the values are z = 26, d = 4 and cs = 3 + 19 = 22. The highest is 26.</span>
<span class="cm-variable">solve</span>(<span class="cm-string">"zodiacs"</span>) <span class="cm-keyword">=</span> <span class="cm-number">26</span>

<span class="cm-variable-2">For</span> <span class="cm-variable">the</span> <span class="cm-variable">word</span> <span class="cm-string">"strength"</span>, <span class="cm-variable">solve</span>(<span class="cm-string">"strength"</span>) <span class="cm-keyword">=</span> <span class="cm-number">57</span>
<span class="cm-comment">-- The consonant substrings are: "str" and "ngth" with values "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. The highest is 57.</span>
</code></pre>
<p>For C: do not mutate input.</p>
<p>More examples in test cases. Good luck!</p>
<p>If you like this Kata, please try:</p>
<p><a href="https://www.codewars.com/kata/598d91785d4ce3ec4f000018" data-turbolinks="false" target="_blank">Word values</a></p>
<p><a href="https://www.codewars.com/kata/59cf8bed1a68b75ffb000026" data-turbolinks="false" target="_blank">Vowel-consonant lexicon</a></p>
