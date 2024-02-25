import io, sys
from htmldiffer import diff

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

try:
    a, b = sys.argv[1:3]
except ValueError:
    print("htmldiffer: highlight the differences between two html files")
    print("usage: " + sys.argv[0] + " a b")
    sys.exit(1)
d = diff.HTMLDiffer(html_a=a, html_b=b, encoding='utf-8')

print(d.combined_diff)
