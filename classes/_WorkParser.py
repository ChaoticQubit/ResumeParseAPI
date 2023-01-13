class _WorkParser:
    def __init__(self, workex, workJson):
        self.workex = workex
        self.workJson = workJson
        self.workHistory = {
            'total_work_experience': self.workex,
            'work_history': []
        }
        for work in self.workJson:
            self.work_dict = {
                'title': '',
                'organization': '',
                'description': '',
                'dates': {
                    'start_date': '',
                    'end_date': '',
                    'is_current': ''
                },
                'location': {
                    'country': '',
                    'city': '',
                    'state': ''
                },
                'metadata': {
                    'job_title': '',
                    'management_level': '',
                    'minor_group': '',
                    'sub_major_group': '',
                    'major_group': '',
                    'group_title': '',
                    'soc_code': ''
                }
            }
            self.__getJobTitle(work.get('job_title', ''))
            self.__getOrganization(work.get('organization', ''))
            self.__getJobDescription(work.get('job_description', ''))
            self.__getDates(work.get('dates', {}))
            self.__getLocation(work.get('location', {}))
            self.__getJobMetadata(work.get('occupation', {}))
            self.workHistory['work_history'].append(self.work_dict)
        
    def __getJobTitle(self, title):
        try:
            self.work_dict['title'] = title
        except:
            self.work_dict['title'] = ''
            
        return self.work_dict['title']
        
    def __getOrganization(self, organization):
        try:
            self.work_dict['organization'] = organization
        except:
            self.work_dict['organization'] = ''

        return self.work_dict['organization']

    def __getJobDescription(self, description):
        try:
            self.work_dict['description'] = description
        except:
            self.work_dict['description'] = ''

        return self.work_dict['description']

    def __getDates(self, dates):
        try:
            self.work_dict['dates']['start_date'] = dates['start_date']
        except:
            self.work_dict['dates']['start_date'] = ''
        try:
            self.work_dict['dates']['end_date'] = dates['end_date']
        except:
            self.work_dict['dates']['end_date'] = ''
        try:
            self.work_dict['dates']['is_current'] = dates['is_current']
        except:
            self.work_dict['dates']['is_current'] = ''
        
        return self.work_dict['dates']
    
    def __getLocation(self, location):
        try:
            self.work_dict['location']['country'] = location['country']
        except:
            self.work_dict['location']['country'] = ''
        try:
            self.work_dict['location']['city'] = location['city']
        except:
            self.work_dict['location']['city'] = ''
        try:
            self.work_dict['location']['state'] = location['state']
        except:
            self.work_dict['location']['state'] = ''

        return self.work_dict['location']
    
    def __getJobMetadata(self, metadata):
        try:
            self.work_dict['metadata']['job_title'] = metadata['job_title_normalized']
        except:
            self.work_dict['metadata']['job_title'] = ''
        try:
            self.work_dict['metadata']['management_level'] = metadata['management_level']
        except:
            self.work_dict['metadata']['management_level'] = ''

        self.__getMetdataClassigication(metadata.get('classification', {}))
            
        return self.work_dict['metadata']
    
    def __getMetdataClassigication(self, metadata):
        try:
            self.work_dict['metadata']['minor_group'] = metadata['minor_group']
        except:
            self.work_dict['metadata']['minor_group'] = ''
        try:
            self.work_dict['metadata']['sub_major_group'] = metadata['sub_major_group']
        except:
            self.work_dict['metadata']['sub_major_group'] = ''
        try:
            self.work_dict['metadata']['major_group'] = metadata['major_group']
        except:
            self.work_dict['metadata']['major_group'] = ''
        try:
            self.work_dict['metadata']['group_title'] = metadata['title']
        except:
            self.work_dict['metadata']['group_title'] = ''
        try:
            self.work_dict['metadata']['soc_code'] = metadata['soc_code']
        except:
            self.work_dict['metadata']['soc_code'] = ''

        return self.work_dict['metadata']

    def getWork(self):
        return self.workHistory