# Hasesa · ሐሰሳ

**An audio-first, offline Amharic tutor for Ethiopian high-school students.**
*Hasesa (ሐሰሳ) — Amharic for "the search / inquiry."*

A student speaks a question in Amharic into a budget phone — with no internet — and hears
an answer grounded in their official Ministry of Education textbook. No data cost, no
account, works on the bus.

This repository is the research groundwork for that vision. It starts small on purpose:
a rigorous study of the single hardest question underneath the whole idea, done on a
laptop with no GPU, before any app is built.

---

## The current study (weeks 1–8)

> **How well can phone-sized language models tutor one high-stakes Ethiopian curriculum
> topic — and does grounding them in the textbook fix what's broken?**

- **Scope:** one chapter, in depth — **Grade 11 Biology, Unit 4: Genetics** (DNA & RNA
  structure, DNA replication, transcription/translation, cell division, inheritance),
  English-medium. ~60 curriculum questions built from the unit's own review questions,
  plus items grounded in a **DNA-extraction lab I ran with Grade 11 students** (see below).
- **Why one chapter, not a whole subject:** depth over breadth. Exhaustively benchmarking a
  single high-stakes unit is more defensible than thin coverage of all of Biology, and it
  lets the failure-mode analysis go deep. The pipeline generalizes to other units unchanged.
- **Experiment:** 4–5 small models (Gemma 3 1B, Llama 3.2 1B, Qwen 2.5 1.5B, + a frontier
  model as a ceiling), each answering in two conditions — *closed-book* (from memory) vs
  *retrieval-grounded* (given the relevant textbook passage).
- **Also measured:** the "tokenizer tax" — how many more tokens Amharic (fidel script)
  costs than English across common tokenizers, which is why small on-device models
  struggle with Amharic.
- **Output:** a short technical report + this public repo + reproducible scripts.

### The classroom anchor — a real lab, not a hypothetical

The benchmark is tied to teaching I actually did: a **DNA-extraction experiment with Grade
11 students in an Ethiopian high school, in collaboration with The Science Basement.** That
gives the study something most curriculum-LLM work lacks — a real, resource-constrained
classroom the tool is meant to serve. It also adds a question category no generic benchmark
has: *can a phone-sized model explain a hands-on experiment the students physically
performed*, in their own language, well enough to reinforce what they saw at the bench?

## Status

🚧 **Not started — planning complete.** Next concrete step: Phase 1 —
locate/download the Grade 11 Biology MoE textbook PDF and extract **Unit 4 (Genetics)**
(the first thing to learn is whether it's clean digital text or scanned images needing OCR).
See `notes/` for the running learning log once work begins.

**Decisions log**
- *Jul 27, 2026:* Scope narrowed from all of Grade 9 Biology to **one chapter — Grade 11
  Biology Unit 4 (Genetics)** — chosen because it's the unit behind the DNA-extraction lab
  run with Grade 11 students and The Science Basement. Depth-over-breadth; ~60 questions
  from the unit's review questions + lab-grounded items.
- *Jul 17, 2026:* Scope fixed — small study (~60 questions, 4–5 models, closed-book vs
  grounded, + tokenizer-tax, degraded-input, and speakability measurements). Deliverable:
  a short technical report + public repo + reproducible scripts; arXiv polish if time
  allows. Non-goals: fine-tuning, Android app, audio integration, multi-subject.

## Layout

| Path | What's in it |
|------|--------------|
| `data/grade11_genetics_questions.txt` | The evaluation set — benchmark items (JSONL, English + Amharic) |
| `data/validate.py` | JSONL validator for the eval set |
| `report/` | The written-up findings (added when the study completes) |

## Data & copyright

The benchmark is built from **Grade 11 Biology, Unit 4 (Genetics)** of the Ethiopian
Ministry of Education textbook. That textbook is copyrighted, so **the PDF and the raw
extracted text are not redistributed here.** The evaluation set stores a **page reference**
(`source_ref`) for each item rather than the textbook passage itself — so the data is
curriculum-grounded and verifiable against your own copy of the textbook, without
republishing copyrighted material. Question stems, Amharic translations, reference answers,
tags, and all code are original to this project.
