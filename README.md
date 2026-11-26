# AI Evaluation & Quality Assurance Portfolio

## 🔄 My AI Evaluation Methodology

```mermaid
graph TD
    A[Define Task & Risks] --> B[Design Rubric & Prompts]
    B --> C[Blind Execution / Data Collection]
    C --> D[Score via Multi-Criteria Rubric]
    D --> E{Calculate Agreement / Kappa}
    E -->|Low Agreement| F[Revise Guidelines]
    E -->|High Agreement| G[Identify Error Patterns]
    G --> H[Propose Engineering Mitigations]
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style H fill:#bbf,stroke:#333,stroke-width:2px

Welcome to my portfolio. This repository documents my progression from foundational AI evaluation frameworks to real-world model testing and safety assessment. 

My goal is to bridge the gap between AI development and reliable, safe, and high-quality user experiences. Every project includes transparent documentation of methodology, limitations, and the use of AI assistants in the workflow.

## Projects

| Project | Focus | Key Deliverables |
|---|---|---|
| **[01-02 Response Evaluation](./01-response-evaluation-framework)** | Rubric Design & Synthetic Testing | Custom 5-criterion rubric, synthetic error cases, accuracy scoring rules. |
| **[03 Model Benchmarking](./03-ai-model-comparison)** | Blind Comparative Testing | Double-blind benchmark plan, randomized scoring, strength/weakness analysis. |
| **[04 Data Annotation Quality](./04-data-annotation-quality)** | Inter-Annotator Agreement | Annotation guidelines, 32-item dataset, Cohen’s Kappa calculation (0.91), guideline revision. |
| **[05 AI Safety & Red Teaming](./05-ai-safety-red-teaming)** | Adversarial Testing | Jailbreak, prompt extraction, and obfuscation test cases with mitigation strategies. |
| **[06 Real-World Evaluation](./06-real-world-evaluation)** | Domain-Specific Assessment | End-to-end evaluation of an LLM on personal finance tasks, identifying math hallucinations and constraint failures. |

## How to Navigate
- Each project folder contains its own `README.md` explaining the objectives, methodology, and findings.
- All projects include a "How this project was made" section, transparently documenting where AI assistance was used for drafting, formatting, or simulating data.

## Contact
- **LinkedIn:** https://www.linkedin.com/in/akanimodavid
- **Email:** davidakan31@gmail.com