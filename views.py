from django.shortcuts import render
from .forms import NumberForm

def index(request):
    result = None

    if request.method == "POST":
        form = NumberForm(request.POST)

        if form.is_valid():
            values = list(form.cleaned_data.values())

            # logical checks
            all_numeric = all(isinstance(x, int) for x in values)
            has_negative = any(x < 0 for x in values)

            average = sum(values) / len(values)
            avg_gt_50 = average > 50

            # count positives
            positive_count = len([x for x in values if x > 0])

            # bitwise even/odd check
            even_or_odd = "Even" if (positive_count & 1) == 0 else "Odd"

            # list >10 sorted
            sorted_values = sorted([x for x in values if x > 10])

            result = {
                "original": values,
                "sorted": sorted_values,
                "average": average,
                "positive_count": positive_count,
                "even_or_odd": even_or_odd,
                "avg_gt_50": avg_gt_50,
                "has_negative": has_negative,
                "all_numeric": all_numeric,
            }

    else:
        form = NumberForm()

    return render(request, "bitwise/index.html",
                  {"form": form, "result": result})