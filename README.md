# Vietnamese Word Vector

* The pretrained word vectors are available [here](https://drive.google.com/open?id=1aIRcRu7YloDjm8f-zaM0ZUCDLzHC0QzI).
* There are 2 types of word vector: unigram and segmented.
* Each of them is trained using 3 methods: CBOW, Skip-gram and GloVe
* To use the unigram word vector, use the `clean_text` function in `preprocess.py` to prepare the texts before mapping them to word vectors.
* To use the segmented version, use [VnCoreNLP](https://github.com/vncorenlp/VnCoreNLP) for word segmentation before mapping them to word vectors.