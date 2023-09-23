Def linearSearchProduct   (productList, targetProduct):
Indices = []

Forindex, product in enumerate(productList): 
Ifproduct == targetProduct:
Indices.append(index)

Return indices


# Example usage:
Products = [“shoes”, “boot”, “loafer”, “shoes”, “sandal”,”shoes”]
Target = “shoes”
Result = linearSearchProduct(products, target)
Print(result