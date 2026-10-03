# normative_release_paper

Theory article for *Religion* (Paper 1 of 3):

**Carry It Without Me: A Cyclical Theory of Normative Internalisation, Normative Release, and Religious Renewal**

Introduces *normative release*: the process by which a norm's reproduction becomes
independent of the continued explicit salience of the religious representation that
transmitted it — distinguished from Anscombe's survival, Nietzsche's shadows,
religion residue, deus otiosus, and vestigial structure theory (Talmont-Kaminski &
Shults, *Religion* 2024). Includes the self-effacement paradox, a norm-specific
cyclical model, and revival-as-selective-reintegration.

## Layout
- `manuscript/manuscript.md` — full manuscript (APA references)
- `manuscript/manuscript_inline.docx` — submission docx, TNR 12pt double-spaced, figures/table inline after first citation, OMML equation
- `manuscript/cover_letter.md` / `.docx` — Religion cover letter
- `figures/make_figures.py` — regenerates fig1–3 PNG (300 dpi) + `figures_editable.pptx`
- `docs/citation_audit.md` — verified bibliography with DOIs
- `docs/novelty_audit.md` — prior-art adjudication per component claim
- `docs/limitations_falsification_audit.md` — falsification conditions + QC checklist

## Rebuild
```bash
pip install python-docx python-pptx matplotlib latex2mathml docx-equation
cd figures && python3 make_figures.py
cd ../manuscript && python3 build_docx.py
```

Paper 2 (religious legibility/measurement) and Paper 3 (Vortex of Mono and Multi)
are out of scope here by design.
