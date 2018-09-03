### Catalogo Backend con Python, Flask-GraphQL

#### Item

```
mutation{
  create_item(item_data: {
    name: "Disco Duro",
    description: "Este es un disco duro de 1 tera"
  }) {
   item{
    name
    description
  }
  }
}
```

#### Area

```
mutation{
  create_area(area_data: {
    name: "C P U",
    description: "Este dato es del area..."
  }) {
   area{
    name
    description
  }
  }
}
```

#### Catalog

```
mutation{
  create_catalog(catalog_data: {
    name: "GC - Hardware	",
    description: "Este dato es de catalogo"
  }) {
   catalog{
    name
    description
  }
  }
}
```
