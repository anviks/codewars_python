<h1 id="roboscript-2---implement-the-rs1-specification">RoboScript #2 - Implement the RS1 Specification</h1>
<h2 id="disclaimer">Disclaimer</h2>
<p>The story presented in this Kata Series is purely fictional; any resemblance to actual programming languages, products, organisations or people should be treated as purely coincidental.</p>
<h2 id="about-this-kata-series">About this Kata Series</h2>
<p>This Kata Series is based on a fictional story about a computer scientist and engineer who owns a firm that sells a toy robot called MyRobot which can interpret its own (esoteric) programming language called RoboScript.  Naturally, this Kata Series deals with the software side of things (I'm afraid Codewars cannot test your ability to build a physical robot!).</p>
<h2 id="story">Story</h2>
<p>Now that you've built your own code editor for RoboScript with appropriate syntax highlighting to make it look like serious code, it's time to properly implement RoboScript so that our MyRobots can execute any RoboScript provided and move according to the will of our customers.  Since this is the first version of RoboScript, let's call our specification RS1 (like how the newest specification for JavaScript is called ES6 :p)</p>
<h2 id="task">Task</h2>
<p>Write an interpreter for RS1 called <code>execute()</code> which accepts 1 required argument <code>code</code>, the RS1 program to be executed.  The interpreter should return a string representation of the smallest 2D grid containing the full path that the MyRobot has walked on (explained in more detail later).</p>
<p>Initially, the robot starts at the middle of a 1x1 grid.  Everywhere the robot walks it will leave a path <code>"*"</code>.  If the robot has not been at a particular point on the grid then that point will be represented by a whitespace character <code>" "</code>.  So if the RS1 program passed in to <code>execute()</code> is empty, then:</p>
<pre><code>""  --&gt;  "*"
</code></pre>
<p>The robot understands 3 major commands:</p>
<ul>
<li><code>F</code> - Move forward by 1 step in the direction that it is currently pointing.  Initially, the robot faces to the right.</li>
<li><code>L</code> - Turn "left" (i.e. <strong>rotate</strong> 90 degrees <strong>anticlockwise</strong>)</li>
<li><code>R</code> - Turn "right" (i.e. <strong>rotate</strong> 90 degrees <strong>clockwise</strong>)</li>
</ul>
<p>As the robot moves forward, if there is not enough space in the grid, the grid should expand accordingly. So:</p>
<pre><code>"FFFFF"  --&gt;  "******"
</code></pre>
<p>As you will notice, 5 <code>F</code> commands in a row should cause your interpreter to return a string containing 6 <code>"*"</code>s in a row.  This is because initially, your robot is standing at the middle of the 1x1 grid facing right.  It leaves a mark on the spot it is standing on, hence the first <code>"*"</code>.  Upon the first command, the robot moves 1 unit to the right.  Since the 1x1 grid is not large enough, your interpreter should expand the grid 1 unit to the right.  The robot then leaves a mark on its newly arrived destination hence the second <code>"*"</code>.  As this process is repeated 4 more times, the grid expands 4 more units to the right and the robot keeps leaving a mark on its newly arrived destination so by the time the entire program is executed, 6 "squares" have been marked <code>"*"</code> from left to right.</p>
<p>Each row in your grid must be separated from the next by a CRLF (<code>\r\n</code>).  Let's look at another example:</p>
<pre><code>"FFFFFLFFFFFLFFFFFLFFFFFL"  --&gt;  "******\r\n*    *\r\n*    *\r\n*    *\r\n*    *\r\n******"
</code></pre>
<p>So the grid will look like this:</p>
<pre><code>******
*    *
*    *
*    *
*    *
******
</code></pre>
<p>The robot moves 5 units to the right, then turns left, then moves 5 units upwards, then turns left again, then moves 5 units to the left, then turns left again and moves 5 units downwards, returning to the starting point before turning left one final time.  Note that the marks do <strong>not</strong> disappear no matter how many times the robot steps on them, e.g. the starting point is still marked <code>"*"</code> despite the robot having stepped on it twice (initially and on the last step).</p>
<p>Another example:</p>
<pre><code>"LFFFFFRFFFRFFFRFFFFFFF"  --&gt;  "    ****\r\n    *  *\r\n    *  *\r\n********\r\n    *   \r\n    *   "
</code></pre>
<p>So the grid will look like this:</p>
<pre><code>    ****
    *  *
    *  *
********
    *
    *
</code></pre>
<p>Initially the robot turns left to face upwards, then moves upwards 5 squares, then turns right and moves 3 squares, then turns right again (to face downwards) and move 3 squares, then finally turns right again and moves 7 squares.</p>
<p>Since you've realised that it is probably quite inefficient to repeat certain commands over and over again by repeating the characters (especially the <code>F</code> command - what if you want to move forwards 20 steps?), you decide to allow a shorthand notation in the RS1 specification which allows your customers to postfix a non-negative integer onto a command to specify how many times an instruction is to be executed:</p>
<ul>
<li><code>Fn</code> - Execute the <code>F</code> command <code>n</code> times (NOTE: <code>n</code> <em>may</em> be more than 1 digit long!)</li>
<li><code>Ln</code> - Execute <code>L</code> n times</li>
<li><code>Rn</code> - Execute <code>R</code> n times</li>
</ul>
<p>So the example directly above can also be written as:</p>
<pre><code>"LF5RF3RF3RF7"
</code></pre>
<p>These 5 example test cases have been included for you :)</p>
<h2 id="kata-in-this-series">Kata in this Series</h2>
<ol>
<li><a href="https://www.codewars.com/kata/roboscript-number-1-implement-syntax-highlighting" data-turbolinks="false" target="_blank">RoboScript #1 - Implement Syntax Highlighting</a></li>
<li><strong>RoboScript #2 - Implement the RS1 Specification</strong></li>
<li><a href="https://www.codewars.com/kata/58738d518ec3b4bf95000192" data-turbolinks="false" target="_blank">RoboScript #3 - Implement the RS2 Specification</a></li>
<li><a href="https://www.codewars.com/kata/594b898169c1d644f900002e" data-turbolinks="false" target="_blank">RoboScript #4 - RS3 Patterns to the Rescue</a></li>
<li><a href="https://www.codewars.com/kata/5a12755832b8b956a9000133" data-turbolinks="false" target="_blank">RoboScript #5 - The Final Obstacle (Implement RSU)</a></li>
</ol>
