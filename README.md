# 💥 PyShield - A Python Obfuscate Tool

**Hard Obfuscate Tool For Python**

# 🤖 Installation
<pre><code>pip install pyshield</code></pre>
And thats it. So east.

# ✨ Quick Start
Printing The Obfuscate Code :
<pre><code>pyshield -f &lt;file_to_obfuscate&gt; -l &lt;level_of_obfuscate&gt; </code></pre>
Save A File :
<pre><code>pyshield -f &lt;file_to_obfuscate&gt; -l &lt;level_of_obfuscate&gt; -o &lt;output_file&gt;</code></pre>
# 🔥 As A Module
Printing The Obfuscated Code : 
<pre><code>from pyshield import PyShield
result = PyShield.obfuscate(file_path,level)
print(result)
</code></pre>
# ☠️ For Windows
<pre><code>from pyshield import PyShield
result = PyShield.obfuscate("example.py",3)
open("result.py","w",encoding='utf8').write(result)
</code></pre>


