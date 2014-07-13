"""
Problem Statement: http://community.topcoder.com/stat?c=problem_statement&pm=13235
"""


class InverseRMQ:
    isImpossible = 'Impossible'
    isPossible = 'Possible'

    def __init_data(self):
        self.__target = []
        self.__exist_item = {}
        self.__current_item = {}


    def possible(self, n, A, B, ans):
        self.__init_data()

        for i in range(len(A)):
            self.__init_current_item(i, A, B, ans)
            if not self.__is_valid_range():
                return InverseRMQ.isImpossible
            if self.__is_value_exist():
                if not self.__is_overlap_to_all():
                    return InverseRMQ.isImpossible
            elif self.__has_overlap():
                for item in self.__target:
                    if self.__is_overlap(item):
                        self.__exist_item = item
                        if not self.__try_reduce_big_value_range():
                            return InverseRMQ.isImpossible

            self.__target.append(self.__current_item)

        if not self.__is_all_data_verify():
            return InverseRMQ.isImpossible
        return InverseRMQ.isPossible

    def __is_value_exist(self):
        for item in self.__target:
            if item['value'] == self.__current_item['value']:
                self.__exist_item = item
                return True
        return False

    def __init_current_item(self, i, A, B, ans):
        self.__current_item = {'value': ans[i], 'start_index': A[i], 'end_index': B[i]}

    def __is_overlap(self, item):
        return self.__current_item['end_index'] >= item['start_index'] and item['end_index'] >= self.__current_item['start_index']

    def __has_overlap(self, target=None):
        if target is None:
            target = self.__target
        for item in target:
            if self.__is_overlap(item):
                return True
        return False

    def __is_overlap_to_all(self):
        for item in self.__target:
            if not self.__is_overlap(item):
                return False
        return True

    def __try_reduce_big_value_range(self):
        if self.__current_item['value'] > self.__exist_item['value']:
            self.__current_item['start_index'] = self.__exist_item['end_index'] + 1
            return self.__current_item['start_index'] <= self.__current_item['end_index']
        elif self.__current_item['value'] < self.__exist_item['value']:
            self.__exist_item['start_index'] = self.__current_item['end_index'] + 1
            return self.__exist_item['start_index'] <= self.__exist_item['end_index']
        else:
            return True

    def __is_valid_range(self):
        return self.__current_item['end_index'] - self.__current_item['start_index'] + 1 <= self.__current_item['value']

    def __is_all_data_verify(self):
        self.__target.sort(key=lambda i: i['value'])
        block = {'width': 0, 'area': []}
        for item in self.__target:
            self.__current_item = item
            if self.__has_overlap(target=block['area']):
                for area in block['area']:
                    if self.__is_overlap(area):
                        old_width = area['end_index'] - area['start_index'] + 1
                        area['start_index'] = min(item['start_index'], area['start_index'])
                        area['end_index'] = max(item['end_index'], area['end_index'])
                        increment_width = area['end_index'] - area['start_index'] + 1 - old_width
                        block['width'] += increment_width
            else:
                block['area'].append(item)
                block['width'] += item['end_index'] - item['start_index'] + 1

            if item['value'] < block['width']:
                return False

        return True