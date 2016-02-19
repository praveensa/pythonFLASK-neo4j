from py2neo import Graph,Node , Relationship

graph=Graph()

user=Node("user",username="Praveen")
post=Node("post",text="Hello world")

graph.create(Relationship(user,"PUBLISHED",post))
