def transform_data(products):
    cleaned_data = []

    for product in products:
        cleaned_data.append({
            "id": product["id"],
            "title": product["title"].strip(),
            "price": float(product["price"]),
            "category": product["category"]
        })

    return cleaned_data
