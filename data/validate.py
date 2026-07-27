import json
ok=err=0
for n,l in enumerate(open('grade11_genetics_questions.txt'),1):
    s=l.strip()
    if not s or s.startswith('#'): continue
    try: json.loads(s); ok+=1
    except json.JSONDecodeError as e: err+=1; print(f'line {n}: {e}')
print(f'valid: {ok}, errors: {err}')