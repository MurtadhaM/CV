# Use Case Diagram

```plantuml
@startuml
left to right direction
skinparam packageStyle rect
actor User
actor Admin
actor "System Admin" as SystemAdmin
rectangle "Use Case Diagram" {
  User -- (Use Case 1)
  User -- (Use Case 2)
  Admin -- (Use Case 3)
  SystemAdmin -- (Use Case 4)
}
@enduml

```
