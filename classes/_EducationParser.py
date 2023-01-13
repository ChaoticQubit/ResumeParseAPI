class _EducationParser:
    def __init__(self, eduJson):
        self.eduJson = eduJson
        self.educationHistory = []
        for edu in self.eduJson:
            self.education_dict = {
                'organization': '',
                'accreditation': {
                    'degree': '',
                    'original_str': '',
                    'education_level': ''
                },
                'grade': {
                    'metric': '',
                    'value': ''
                },
                'location': {
                    'country': '',
                    'city': '',
                    'state': ''
                },
                'dates': {
                    'start_date': '',
                    'end_date': '',
                    'is_current': ''
                }
            }
            self.__getOrganization(edu.get('organization', ''))
            self.__getAccreditation(edu.get('accreditation', {}))
            self.__getGrades(edu.get('grade', {}))
            self.__getLocation(edu.get('location', {}))
            self.__getDates(edu.get('dates', {}))
            self.educationHistory.append(self.education_dict)
    
    def __getOrganization(self, organization):
        try:
            self.education_dict['organization'] = organization
        except:
            self.education_dict['organization'] = ''

        return self.education_dict['organization']
    
    def __getAccreditation(self, accreditation):
        self.education_dict['accreditation']['original_str'] = accreditation['input_str']
        try:
            self.education_dict['accreditation']['degree'] = accreditation['education']
        except:
            self.education_dict['accreditation']['degree'] = ''
        try:
            self.education_dict['accreditation']['education_level'] = accreditation['education_level']
        except:
            self.education_dict['accreditation']['education_level'] = ''
    
        return self.education_dict['accreditation']

    def __getGrades(self, grades):
        try:
            self.education_dict['grade']['metric'] = grades['metric']
        except:
            self.education_dict['grade']['metric'] = ''
        try:
            self.education_dict['grade']['value'] = grades['value']
        except:
            self.education_dict['grade']['value'] = ''
        
        return self.education_dict['grade']

    def __getLocation(self, location):
        try:
            self.education_dict['location']['country'] = location['country']
        except:
            self.education_dict['location']['country'] = ''
        try:
            self.education_dict['location']['city'] = location['city']
        except:
            self.education_dict['location']['city'] = ''
        try:
            self.education_dict['location']['state'] = location['state']
        except:
            self.education_dict['location']['state'] = ''

        return self.education_dict['location']

    def __getDates(self, dates):
        try:
            self.education_dict['dates']['start_date'] = dates['start_date']
        except:
            self.education_dict['dates']['start_date'] = ''
        try:
            self.education_dict['dates']['end_date'] = dates['completion_date']
        except:
            self.education_dict['dates']['end_date'] = ''
        try:
            self.education_dict['dates']['is_current'] = dates['is_current']
        except:
            self.education_dict['dates']['is_current'] = ''
        
        return self.education_dict['dates']
    
    def getEducation(self):
        return self.educationHistory