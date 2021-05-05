from abc import ABC


class Band:
    all_bands= []
    
    def __init__(self,name,members):
        self.name = name
        self.members = members
        Band.all_bands.append({'name':name,'members':members})
    
    def play_solos(self):
        solos_arr=[]
        for member_obj in self.members:
            check = str(member_obj).split()[-1]
            if check == 'guitar': solos_arr.append('face melting guitar solo')
            elif check == 'bass': solos_arr.append('bom bom buh bom')
            else:
                solos_arr.append('rattle boom crash')
        return solos_arr
        
    def __str__(self):
        return f"The band {self.name} has the following members {self.members.join(',')}"
    
    def __repr__(self):
        return f'<band: {self.name}> <members: {self.members.join(",")}>'
    
    @classmethod
    def to_list(cls):
        return cls.all_bands


class Musician:
    members=[]
    
    def __init__(self,name,instrument,job,solo_play):
        self.name=name
        self.job=job
        self.instrument=instrument
        self.solo_play = solo_play
        Musician.members.append(name)
    
    def __str__(self):
        return f'My name is {self.name} and I play {self.instrument}'
    
    def __repr__(self):
        return f'{self.job} instance. Name = {self.name}'
    
    def get_instrument(self):
        return f'{self.instrument}'
    
    def play_solo(self):
        return f'{self.solo_play}'


class Guitarist(Musician):
    job= 'Guitarist'
    instrument = 'guitar'
    solo_play = 'face melting guitar solo'
    
    def __init__(self, name):
        super().__init__(name,Guitarist.instrument,Guitarist.job,Guitarist.solo_play)


class Bassist(Musician):
    job= 'Bassist'
    solo_play = 'bom bom buh bom'
    instrument = 'bass'

    def __init__(self, name):
        super().__init__(name,Bassist.instrument,Bassist.job,Bassist.solo_play)


class Drummer(Musician):
    job= 'Drummer'
    instrument = 'drums'
    solo_play = 'rattle boom crash'

    def __init__(self, name):
        super().__init__(name,Drummer.instrument,Drummer.job,Drummer.solo_play)