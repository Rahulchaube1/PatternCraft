# Update README with enhanced header badges and author sponsorship footer
import re

readme_path = r"C:\Users\Rahul Chaube\Downloads\design-patterns-for-humans-master\readme.md"

with open(readme_path, "r", encoding="utf-8") as f:
    text = f.read()

# Replace the top badges with high-impact open source badges
old_header_badges = """<p align="center">
  <a href="#-creational-design-patterns"><img src="https://img.shields.io/badge/Creational-6_Patterns-0284c7?style=flat-square" alt="Creational" /></a>
  <a href="#-structural-design-patterns"><img src="https://img.shields.io/badge/Structural-7_Patterns-6366f1?style=flat-square" alt="Structural" /></a>
  <a href="#-behavioral-design-patterns"><img src="https://img.shields.io/badge/Behavioral-10_Patterns-059669?style=flat-square" alt="Behavioral" /></a>
  <a href="#-solid-principles-alignment"><img src="https://img.shields.io/badge/Architecture-SOLID_Aligned-f59e0b?style=flat-square" alt="SOLID" /></a>
  <a href="#-pattern-decision-matrix"><img src="https://img.shields.io/badge/Decision_Guide-Included-10b981?style=flat-square" alt="Guide" /></a>
</p>"""

new_header_badges = """<p align="center">
  <a href="https://github.com/Rahulchaube1/PatternCraft/stargazers"><img src="https://img.shields.io/github/stars/Rahulchaube1/PatternCraft?style=for-the-badge&logo=github&color=38bdf8&logoColor=white" alt="GitHub Stars" /></a>
  <a href="https://github.com/Rahulchaube1/PatternCraft/network/members"><img src="https://img.shields.io/github/forks/Rahulchaube1/PatternCraft?style=for-the-badge&logo=github&color=818cf8&logoColor=white" alt="GitHub Forks" /></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-MIT-10b981?style=for-the-badge&logo=opensourceinitiative&logoColor=white" alt="License MIT" /></a>
  <a href="./CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-Welcome-f59e0b?style=for-the-badge&logo=git&logoColor=white" alt="PRs Welcome" /></a>
  <a href="https://buymeacoffee.com/rahulchaube"><img src="https://img.shields.io/badge/Buy_Me_A_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me A Coffee" /></a>
  <a href="https://rahulchaube1.com"><img src="https://img.shields.io/badge/Author-Rahul_Chaube-0284c7?style=for-the-badge&logo=safari&logoColor=white" alt="Author Portfolio" /></a>
</p>

<p align="center">
  <a href="#-creational-design-patterns"><img src="https://img.shields.io/badge/Creational-6_Patterns-0284c7?style=flat-square" alt="Creational" /></a>
  <a href="#-structural-design-patterns"><img src="https://img.shields.io/badge/Structural-7_Patterns-6366f1?style=flat-square" alt="Structural" /></a>
  <a href="#-behavioral-design-patterns"><img src="https://img.shields.io/badge/Behavioral-10_Patterns-059669?style=flat-square" alt="Behavioral" /></a>
  <a href="#-solid-principles-alignment"><img src="https://img.shields.io/badge/Architecture-SOLID_Aligned-f59e0b?style=flat-square" alt="SOLID" /></a>
  <a href="#-architectural-selection-flowchart"><img src="https://img.shields.io/badge/Decision_Guide-Included-10b981?style=flat-square" alt="Guide" /></a>
</p>"""

text = text.replace(old_header_badges, new_header_badges)

# Replace the footer with the comprehensive Author, Connect, Sponsorship, and Open-Source section
footer_start = text.find("## 🤝 Community & Architectural Contributions")
if footer_start == -1:
    footer_start = text.find("## dY ? Community")

new_footer = """## 🤝 Community & Open-Source Contributions

**PatternCraft** thrives because of engineers, educators, and open-source contributors around the globe:
- 💡 **Open an Issue** on [GitHub Issues](https://github.com/Rahulchaube1/PatternCraft/issues) to report bugs, suggest architecture refinements, or propose new design paradigms.
- 🚀 **Submit a Pull Request** with language implementations (Python, TypeScript, Go, Rust, Java, C#) by checking out our [Contributing Guide](CONTRIBUTING.md).
- ⭐ **Star this Repository:** If this guide leveled up your understanding of system design, architecture, or object-oriented software engineering, please star the project on [GitHub](https://github.com/Rahulchaube1/PatternCraft)!

---

## 👨‍💻 Author & Maintainer

<table border="0">
  <tr>
    <td width="100" align="center" valign="middle">
      <img src="https://github.com/Rahulchaube1.png?size=140" width="90" style="border-radius: 50%;" alt="Rahul Chaube" />
    </td>
    <td valign="middle">
      <h3>Rahul Chaube</h3>
      <p>Software Engineer &amp; Systems Architect dedicated to building robust developer ecosystems, high-scale software architectures, and open-source tools.</p>
      <p>
        <a href="https://rahulchaube1.com"><img src="https://img.shields.io/badge/Portfolio-rahulchaube1.com-0284c7?style=flat-square&logo=google-chrome&logoColor=white" alt="Portfolio" /></a>
        <a href="https://github.com/Rahulchaube1"><img src="https://img.shields.io/badge/GitHub-@Rahulchaube1-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub" /></a>
        <a href="https://www.linkedin.com/in/rahulchaube1/"><img src="https://img.shields.io/badge/LinkedIn-Rahul_Chaube-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
        <a href="https://buymeacoffee.com/rahulchaube"><img src="https://img.shields.io/badge/Support-Buy_Me_A_Coffee-FFDD00?style=flat-square&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me A Coffee" /></a>
      </p>
    </td>
  </tr>
</table>

### 🌐 Connect & Follow
* **Portfolio:** [https://rahulchaube1.com](https://rahulchaube1.com)
* **GitHub:** [https://github.com/Rahulchaube1](https://github.com/Rahulchaube1)
* **LinkedIn:** [https://www.linkedin.com/in/rahulchaube1/](https://www.linkedin.com/in/rahulchaube1/)
* **Buy Me a Coffee:** [https://buymeacoffee.com/rahulchaube](https://buymeacoffee.com/rahulchaube)

---

## 💖 Sponsorship & Product Collaborations

Are you building an innovative engineering product, SaaS platform, or developer tool? We love partnering with technical teams and sponsors who value clean code, developer experience, and open source:

- 💎 **Sponsor PatternCraft:** Support continuous development, interactive visual tools, and multi-language expansions.
- 🛠️ **Product Engineering & Architecture Consulting:** Partner with Rahul Chaube for systems design reviews, architectural advisory, and high-impact engineering leadership.
- 📬 **Get in Touch:** Reach out directly through [rahulchaube1.com](https://rahulchaube1.com) or message on [LinkedIn](https://www.linkedin.com/in/rahulchaube1/).

---

## 📜 Open Source License

This project is open-source and free for everyone, licensed under the **[MIT License](LICENSE)**.

```
MIT License
Copyright (c) 2026 Rahul Chaube (https://rahulchaube1.com)
```

Permission is granted to freely use, modify, distribute, and integrate this guide into educational curricula, team engineering wikis, and software projects worldwide.
"""

if footer_start != -1:
    text = text[:footer_start] + new_footer
else:
    text = text + "\n\n" + new_footer

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated README successfully!")
