def linkedSearchProduct(productList, targetProduct) :
  indices=[]
  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)
  return indices



product =["shoes","boat","loafer","shoes", "sandal","shoes"]
target="shoes"
target='apple'
result =linkedSearchProduct (product, target)
print (result)