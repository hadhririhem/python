from store import Store

library = Store("library")
library.add_product("pen", "pen", 2, "pencils")
library.add_product("journal", "journal", 0.50, "Journals")
library.add_product("book", "book", 2.50, "history")
library.inflation(4)
library.set_clearence("pencils", 4)
print("unique id")
library.sell_product(1)
