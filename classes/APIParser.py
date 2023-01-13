from classes._ResumeConversion import _ResumeConversion
from classes._EducationParser import _EducationParser
from classes._WorkParser import _WorkParser
from classes._SkillParser import _SkillParser

class APIParser(_ResumeConversion):
    def __init__(self, sas_url):
        super().__init__(sas_url)
        self.resume_dict = {
            'name': {
                'first_name': '',
                'middle_name': '',
                'last_name': '',
                'title': ''
            },
            'phone': [],
            'email': [],
            'website': [],
            'location': {
                'city': '',
                'state': '',
                'country': '',
                'zipcode': '',
                'street': '',
                'street_number': '',
                'apartment': ''
            },
            'languages': [],
            'summary': {
                'objective': '',
                'summary': ''
            },
            'education': [],
            'work_experience': {},
            'skills': [],
            'certifications': [],
            'awards': [],
            'publications': [],
            'references': [],
            'projects': '',
            'extracurriculars': '',
        }
        self.__getName()
        self.__getPhones()
        self.__getEmails()
        self.__getWebsites()
        self.__getLocation()
        self.__getLanguages()
        self.__getSummary()
        self.__getEducationHistory()
        self.__getWorkHistory()
        self.__getSkills()
        self.__getCertifications()
        self.__getAwards()
        self.__getPublications()
        self.__getReferences()
        self.__getProjects()
        self.__getExtracurriculars()
        
    def __getName(self):
        try:
            self.resume_dict['name']['first_name'] = self.resumeJson['name']['first']  
        except:
            self.resume_dict['name']['first_name'] = ''

        try:
            self.resume_dict['name']['middle_name'] = self.resumeJson['name']['middle']
        except:
            self.resume_dict['name']['middle_name'] = ''

        try:
            self.resume_dict['name']['last_name'] = self.resumeJson['name']['last']
        except:
            self.resume_dict['name']['last_name'] = ''

        try:
            self.resume_dict['name']['title'] = self.resumeJson['name']['title']
        except:
            self.resume_dict['name']['title'] = ''
        
    def __getPhones(self):
        try:
            self.resume_dict['phone'] = self.resumeJson['phone_numbers']
        except:
            self.resume_dict['phone'] = []
    
    def __getEmails(self):
        try:
            self.resume_dict['email'] = self.resumeJson['emails']
        except:
            self.resume_dict['email'] = []

    def __getWebsites(self):
        try:
            self.resume_dict['website'] = self.resumeJson['websites']
        except:
            self.resume_dict['website'] = []
    
    def __getLocation(self):
        try:
            self.resume_dict['location']['city'] = self.resumeJson['location']['city']
        except:
            self.resume_dict['location']['city'] = ''

        try:
            self.resume_dict['location']['state'] = self.resumeJson['location']['state']
        except:
            self.resume_dict['location']['state'] = ''
        
        try:
            self.resume_dict['location']['country'] = self.resumeJson['location']['country']
        except:
            self.resume_dict['location']['country'] = ''
        
        try:
            self.resume_dict['location']['zipcode'] = self.resumeJson['location']['postal_code']
        except:
            self.resume_dict['location']['zipcode'] = ''

        try:
            self.resume_dict['location']['street'] = self.resumeJson['location']['street']
        except:
            self.resume_dict['location']['street'] = ''

        try:
            self.resume_dict['location']['street_number'] = self.resumeJson['location']['street_number']
        except:
            self.resume_dict['location']['street_number'] = ''

        try:
            self.resume_dict['location']['apartment'] = self.resumeJson['location']['apartment_number']
        except:
            self.resume_dict['location']['apartment'] = ''
    
    def __getLanguages(self):
        try:
            self.resume_dict['languages'] = self.resumeJson['languages']
        except:
            self.resume_dict['languages'] = []
        
    def __getSummary(self):
        try:
            self.resume_dict['summary']['objective'] = self.resumeJson['objective']
        except:
            self.resume_dict['summary']['objective'] = ''
        
        try:
            self.resume_dict['summary']['summary'] = self.resumeJson['summary']
        except:
            self.resume_dict['summary']['summary'] = ''
        
    def __getEducationHistory(self):
        try:
            edu = _EducationParser(self.resumeJson['education'])
            self.resume_dict['education'] = edu.getEducation()
        except:
            self.resume_dict['education'] = []
    
    def __getWorkHistory(self):
        try:
            work = _WorkParser(self.resumeJson['total_years_experience'], self.resumeJson['work_experience'])
            self.resume_dict['work_experience'] = work.getWork()
        except:
            self.resume_dict['work_experience'] = []

    def __getSkills(self):
        try:
            skill = _SkillParser(self.resumeJson['skills'], self.resumeJson['sections'])
            self.resume_dict['skills'] = skill.getSkills()
        except:
            self.resume_dict['skills'] = []

    def __getCertifications(self):
        try:
            self.resume_dict['certifications'] = self.resumeJson['certifications']
        except:
            self.resume_dict['certifications'] = []

    def __getAwards(self):
        sections = self.resumeJson['sections']
        try:
            generator = (section for section in sections if "Achievements" in section["section_type"])
            self.resume_dict['awards'] = generator.__next__()["text"]
        except:
            self.resume_dict['awards'] = []

    def __getPublications(self):
        try:
            self.resume_dict['publications'] = self.resumeJson['publications']
        except:
            self.resume_dict['publications'] = []

    def __getReferences(self):
        try:
            for refer in self.resumeJson['referees']:
                referenceDict = {
                    'name': '',
                    'text': '',
                    'phone': '',
                    'email': ''
                }
                referenceDict['name'] = refer['name']
                referenceDict['text'] = refer['text']
                referenceDict['phone'] = refer['number']
                referenceDict['email'] = refer['email']
                self.resume_dict['references'].append(referenceDict)
        except:
            self.resume_dict['references'] = []

    def __getProjects(self):  
        sections = self.resumeJson['sections']
        try:
            generator = (section for section in sections if "Projects" in section["section_type"])
            self.resume_dict['projects'] = generator.__next__()["text"]
        except:
            self.resume_dict['projects'] = []

    def __getExtracurriculars(self):
        sections = self.resumeJson['sections']
        try:
            generator = (section for section in sections if "Extracurriculars" in section["section_type"])
            self.resume_dict['extracurriculars'] = generator.__next__()["text"]
        except:
            self.resume_dict['extracurriculars'] = []

    def getResume(self):
        return self.resume_dict