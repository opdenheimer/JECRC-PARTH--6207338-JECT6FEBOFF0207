import time

class TODO:

    # todos = [
    #     {'id': '',
    #      'desc': '',
    #      'is_completed': False
    #      }, {}, {}, {}
    # ]
    todos = []

    def add_todo(self, desc):
        ## 1. Take the desc from the user.
        ## 2. We have to create one dictionary in which we will add the todo desc.
        ## 3. We have to append that dictionary inside todos.
        if len(desc)<=0:
            print("No Description Entered")
        todo={'id':int(time.time()),"desc":desc,"is_completed":False}
        self.todos.append(todo)
        return self.todos
    
    def remove_todo(self, id):
        for i in self.todos:
            if (i['id'] ==id ):
                self.todos.remove(i)
        print("specified id removed") 
        return self.todos       



    
    def display_todos(self):
        print(f"here is your todos {self.todos}")
    
    def update_todo(self, id, new_desc):
        for i in self.todos:
            if i['id']==id:
                i['desc']=new_desc
                return self.todos
        return f"id Not present in todos"
    
    def toggle_mark_as_completed(self, id):
        for i in self.todos:
            if i['id']==id:
                i['is_completed']=True
                return self.todos
        return f"id Not present in todos"

        
    
    def completed_todos(self):
        if len(self.todos)==0: return
        for i in self.todos:
            if i['is_completed']==True:
                return f"Complete--> {i['desc']}"
        
    
    def incompleted_todos(self):
       if len(self.todos)==0: return
       for i in self.todos:
            if i['is_completed']==False:
                return f"incomplete--> {i['desc']}"
    

obj=TODO()
print(obj.add_todo("here is the desc"))
print(obj.update_todo(obj.todos[0]['id'],"trying to update the todo"))
print(obj.display_todos())
print(obj.completed_todos())
print(obj.incompleted_todos())
print(obj.toggle_mark_as_completed(obj.todos[0]['id']))