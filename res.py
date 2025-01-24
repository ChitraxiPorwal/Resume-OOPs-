from fpdf import FPDF

class Resume:
    def __init__(self):
        self.name = " "
        self.email = " "
        self.phone = " "
        self.github = " "
        self.linkedin = " "
        self.objectives = " "
        self.education = []
        self.skills = []
        self.workex = []
        self.projects = []
        self.awards = []
        self.hobbies = []

    def personal_details(self):
        print("\n****************************** Enter your Personal Details ******************************\n")
        self.name = input("Enter your name: ")
        self.email = input("Enter your email: ")
        self.phone = input("Enter your phone no.: ")
        self.github = input("Enter your github id: ")
        self.linkedin = input("Enter your linkedin id: ")

    def objective_details(self):
        print("\n****************************** Enter your Objective ******************************\n")
        ans = input("Do you want to include Objective in your resume y/n :").strip().lower()               
        if (ans == 'y'):              
            self.objectives = input("Enter objective for your resume:")

    def educational_details(self):
        print("\n****************************** Enter your Educational Details ******************************\n")
        ans = 'y'
        while (ans == 'y'):
            ans = input("Do you want to include Educational Details y/n :").strip().lower()
            if (ans == 'y'):              
                institution = input("Enter you college/school name:")
                program = input("Enter programme you have done:")
                marks = input("Enter your marks in that program:")
                self.education.append(f"{institution},{program},{marks}")

    def skills_details(self):
        print("\n****************************** Enter your Skills ******************************\n")
        ans = 'y'
        while (ans == 'y'):
            ans = input("Do you want to enter Skills y/n :").strip().lower()
            if (ans == 'y'):              
                skill = input("Enter your skills:")
                self.skills.append(f"{skill}")

    def work_experiences(self):
        print("\n****************************** Enter your Working Experiences ******************************\n")
        ans = 'y'
        while (ans == 'y'):
            ans = input("Do you want to enter working experiences  y/n :").strip().lower()
            if (ans == 'y'):              
                company = input("Enter company name:")
                post = input("Enter your post:")
                self.workex.append(f"{company} , {post}")

    def project_details(self):
        print("\n****************************** Enter your Project Details ******************************\n")
        ans = 'y'
        while (ans == 'y'):
            ans = input("Do you want to enter Project Details  y/n :").strip().lower()
            if (ans == 'y'):              
                proj = input("Enter your project name:")
                tech = input("Enter technology used:")
                desc = input("Enter description of your project:")
                self.projects.append(f"{proj},{tech},{desc}")

    def award_achievements(self):
        print("\n****************************** Enter your Awards and Achievements ******************************\n")
        ans = 'y'
        while (ans == 'y'):
            ans = input("Do you want to enter Awards and Achievements  y/n :").strip().lower()
            if (ans == 'y'):               
                award = input("Enter your awards you ever received:")
                self.awards.append(f"{award}")

    def hobbies_interests(self):
        print("\n****************************** Enter your Hobbies and Interests ******************************\n")
        ans = 'y'
        while (ans == 'y'):
            ans = input("Do you want to enter Awards and Achievements  y/n :").strip().lower()
            if (ans == 'y'):               
                hobby = input("Enter your hobbies:")
                self.hobbies.append("Enter your hobbies:")

    def display(self):
        dis = "\n****************************** RESUME ******************************\n"
        dis += f"Personal Details:\n\n{self.name}\n{self.email}\n{self.phone}\n{self.linkedin}\n{self.github}"
        
        if self.objectives:
            dis += f"\n\nobjectives:\n{self.objectives}"
            
        if self.education:
            dis += f"\n\nEducational Details:\n" + "\n" .join(self.education)

        if self.skills:
            dis += f"\n\nSkills:\n" + "\n" .join(self.skills)

        if self.workex:
            dis += f"\n\nWork Experiences:\n" + "\n" .join(self.workex)

        if self.projects:
            dis += f"\n\nProject Details:\n" + "\n" .join(self.projects)

        if self.awards:
            dis += f"\n\nAwards and Achievements:\n" + "\n" .join(self.awards)
                
        if self.hobbies:
            dis += f"\n\nHobbies and Interests:\n" + "\n" .join(self.hobbies)

        print(dis)
        return dis
   
       
    def pdf(self, content, filename="NEW.pdf"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=13)
        
        for line in content.split("\n"):
            pdf.cell(200, 10, txt=line, ln=True)
            
        pdf.output(filename)
        
        print("According to information you have entered resume have been generated as the name:" + filename + ".pdf")
        

if __name__ == "__main__":
    res = Resume()
    res.personal_details()
    res.objective_details()
    res.educational_details()
    res.skills_details()
    res.work_experiences()
    res.project_details()
    res.award_achievements()
    res.hobbies_interests()
    res_con = res.display()
    res.pdf(res_con)
    

    
    