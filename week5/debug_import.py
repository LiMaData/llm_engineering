import sys
print(f"Python Executable: {sys.executable}")
try:
    import sentence_transformers
    print("Successfully imported sentence_transformers")
    print(f"Version: {sentence_transformers.__version__}")
except ImportError as e:
    print(f"Failed to import sentence_transformers: {e}")

try:
    from langchain_huggingface import HuggingFaceEmbeddings
    print("Successfully imported HuggingFaceEmbeddings")
except ImportError as e:
    print(f"Failed to import HuggingFaceEmbeddings: {e}")
