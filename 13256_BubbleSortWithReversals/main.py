"""
Problem Statement: http://community.topcoder.com/stat?c=problem_statement&pm=13256
"""
__author__ = 'Peter Liang'

import math


class BubbleSortWithReversals:
    def __init__(self):
        self.targetList = []
        self.candidate_list = []

    def getMinSwaps(self, A, K):
        self.targetList = A
        self.get_reverse_candidate()
        for i in range(K):
            if not self.candidate_list:
                break
            current_max = max(self.candidate_list, key=lambda k: k["length"])
            for index, value in enumerate(self.candidate_list):
                if value == current_max:
                    self.reverse_slice(value["start_index"], value["end_index"])
                    del self.candidate_list[index]
                    break
        return self.bubble_sort()

    def bubble_sort(self):
        swap_count = 0
        for i in range(len(self.targetList)):
            for j in range(len(self.targetList) - 1):
                if self.targetList[j] > self.targetList[j + 1]:
                    self.targetList[j], self.targetList[j + 1] = self.targetList[j + 1], self.targetList[j]
                    swap_count += 1
        return swap_count

    def reverse_slice(self, start, end):
        for i in range(0, math.ceil((end - start) / 2)):
            self.targetList[start + i], self.targetList[end - i] = self.targetList[end - i], self.targetList[start + i]

    def get_reverse_candidate(self):
        start_index = end_index = 0
        start_value = end_value = self.targetList[start_index]
        for index, value in enumerate(self.targetList):
            if value <= end_value:
                end_index = index
                end_value = value
            elif value > end_value:
                if end_index - start_index > 0:
                    candidate = {"start_index": start_index, "start_value": start_value, "end_index": end_index, "end_value": end_value, "length": end_index - start_index}
                    self.candidate_list.append(candidate)
                start_index = end_index = index
                start_value = end_value = value
        if end_index - start_index > 0:
            candidate = {"start_index": start_index, "start_value": start_value, "end_index": end_index, "end_value": end_value, "length": end_index - start_index}
            self.candidate_list.append(candidate)
