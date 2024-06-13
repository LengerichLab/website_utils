"""
Utilities for making a word cloud from:
    - a text string
    - a bibtex file with entries containing 'abstract' tags
"""

import os

import bibtexparser
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def make_word_cloud_from_text(
    text, img_output_dir=".", img_fname="easy_word_cloud.png", show=True
):
    """Create a word cloud from a string."""
    wordcloud = WordCloud(
        width=2000,
        height=800,
        background_color="white",
        stopwords=None,
        min_font_size=10,
    ).generate(text)

    # Plot the word cloud
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    if show:
        plt.show()

    # Save the word cloud
    if img_output_dir and img_fname:
        os.makedirs(img_output_dir, exist_ok=True)
        wordcloud.to_file(f"{img_output_dir}/{img_fname}")


def make_word_cloud_from_bibtex(
    relative_bib_url,
    img_output_dir=".",
    img_fname="easy_word_cloud.png",
    all_abstracts_fname="all_abstracts.txt",
    show=True,
):
    """Create a word cloud from the abstracts of all the publications in the bib file."""
    all_abstracts = []
    bib_data = bibtexparser.parse_file(relative_bib_url)
    for entry in bib_data.entries:
        bib_id = entry["ID"]
        if bib_id:  # Ensure bib_id exists (i.e. it's a real bib entry)
            try:
                abstract = entry["abstract"]
                all_abstracts.append(abstract)
            except KeyError:
                pass

    if all_abstracts_fname:
        with open(all_abstracts_fname, "w", encoding="utf-8") as g:
            g.write("\n".join(all_abstracts))

    make_word_cloud_from_text(" ".join(all_abstracts), img_output_dir, img_fname, show)
