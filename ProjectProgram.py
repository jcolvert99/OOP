import ProjectClass as p

proj1 = p.Project(1001, 'SAP Implementation', 25, '09/30/2022')
proj2 = p.Project(1002, 'Migration to CRM', 10, '06/30/2022')

projDict = {proj1.get_ID(): proj1.get_dueDate(),
            proj2.get_ID(): proj2.get_dueDate()}

print(projDict)
