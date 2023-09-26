def linearSearchProduct(productList,targetProduct):
    indices=[]
    for index,product in enumerate(productList):

         if product==targetproduct:
             indices.append(index)
         return indics

#Example usage:
        products=["shoes","boot","losgrt","shoes","sandal","shoes"]
        target="shoes"
        target2='apple'
        result=linearSearchProduct(products,target)
        print(result)

        
