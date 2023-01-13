class _SkillParser:
    def __init__(self, skillText, sections):
        self.skillText = skillText
        self.skills = []
        self.section = ''
        self.section = (section for section in sections if "Skills" in section["section_type"]).__next__()["text"].lower()
        self.__getSkillNames()
        self.unparsedSkills = self.__getUnparsedSkills()
        self.__mergeSkills()

    def __getSkillNames(self):
        for skill in self.skillText:
            self.skills.append(skill["name"])

        return self.skills
    
    def __getUnparsedSkills(self):
        keywords = ["skills", "cetification", "certifications", "skill", "technical", "soft", "hard"]
        for keyword in keywords:
            if keyword in self.section:
                self.section = self.section.replace(keyword, "")
        self.section = self.section.replace(":", "")
        self.section = self.section.replace(";", "")
        self.section = self.section.strip()
        unparsedSkills = self.section.split(",")
        unparsedSkills = [skill.strip() for skill in unparsedSkills]
        return unparsedSkills

    def __mergeSkills(self):
        for unparsedSkill in self.unparsedSkills:
            if unparsedSkill not in self.skills:
                self.skills.append(unparsedSkill)
        return self.skills

    
    def getSkills(self):
        return self.skills