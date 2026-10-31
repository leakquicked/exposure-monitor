import argparse,json,re
from pathlib import Path
RULES=[["admin","\\b(admin panel public|public admin|exposed management)\\b","high"],["service","\\b(open port|publicly exposed|internet-facing)\\b","medium"],["secret","\\b(api[_ -]?key|password|secret|token)\\s*[:=]\\s*\\S+","critical"]]
def analyze_text(text):
 out=[]
 for rule,pattern,severity in RULES:
  for m in re.finditer(pattern,text,re.I): out.append({"rule":rule,"severity":severity,"line":text.count("\\n",0,m.start())+1,"match":m.group(0)[:120]})
 return out
def main():
 p=argparse.ArgumentParser(description="Review asset-inventory notes for exposure markers");p.add_argument("input",type=Path);p.add_argument("--output",type=Path);a=p.parse_args()
 if not a.input.is_file(): p.error("input file not found")
 findings=analyze_text(a.input.read_text(encoding="utf-8",errors="replace"));report={"tool":"exposure-monitor","count":len(findings),"findings":findings};data=json.dumps(report,indent=2,ensure_ascii=False)
 if a.output:a.output.write_text(data+"\\n",encoding="utf-8")
 print(data)
if __name__=="__main__":main()
