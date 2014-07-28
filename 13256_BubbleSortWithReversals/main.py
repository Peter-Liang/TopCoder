"""
Problem Statement: http://community.topcoder.com/stat?c=problem_statement&pm=13256
"""
__author__ = 'Peter Liang'

import math
import copy


class BubbleSortWithReversals:
    def __init__(self):
        self.__targetList = []
        self.__candidate_list = []
        self.__best_group = []
        self.__reversed_target = []

    def getMinSwaps(self, A, K):
        self.__init__()
        self.__targetList = A
        self.__get_reverse_candidate()
        self.__get_best_group(K)
        self.__reverse_target()
        return self.__get_min_sort_time()

    def __bubble_sort(self, target_list=None):
        if not target_list:
            target_list = self.__targetList
        swap_count = 0
        for i in range(len(target_list)):
            for j in range(len(target_list) - 1):
                if target_list[j] > target_list[j + 1]:
                    target_list[j], target_list[j + 1] = target_list[j + 1], target_list[j]
                    swap_count += 1
        return swap_count

    def __reverse_slice(self, start, end, target_list=None):
        if not target_list:
            target_list = self.__targetList
        for i in range(0, math.ceil((end - start) / 2)):
            target_list[start + i], target_list[end - i] = target_list[end - i], target_list[start + i]

    def __get_reverse_candidate(self):
        index = 0
        for start_index in range(len(self.__targetList)):
            for end_index in range(len(self.__targetList)):
                score = self.__get_reverse_score(start_index, end_index)
                if score > 0:
                    self.__candidate_list.append({"start_index": start_index, "end_index": end_index, "score": score})
                    index += 1

    def __get_reverse_score(self, start_index, end_index):
        score = 0
        for i in range(0, math.ceil((end_index - start_index) / 2)):
            if self.__targetList[start_index + i] > self.__targetList[end_index - i]:
                score += 1
            elif self.__targetList[start_index + i] < self.__targetList[end_index - i]:
                score -= 1
        return score

    def __get_best_group(self, k):
        best_score = 0
        for combination_count in range(1, min(k, len(self.__candidate_list)) + 1):
            candidate_groups = self.__get_all_group(0, len(self.__candidate_list), combination_count)
            for group in candidate_groups:
                group_score = self.__get_group_score(group)
                if group_score < best_score:
                    continue
                if group_score > best_score:
                    best_score = group_score
                    self.__best_group = []
                self.__best_group.append(group)


    def __get_all_group(self, start, end, count):
        groups = []
        if count == 1:
            for i in range(start, end):
                groups.append(i)
        else:
            for i in range(start, end):
                sub_group = self.__get_all_group(i + 1, end, count - 1)
                for k in range(len(sub_group)):
                    if type(sub_group[k]) is int:
                        groups.append([i, sub_group[k]])
                    else:
                        groups.append([i] + (sub_group[k]))
        return groups

    def __get_group_score(self, group):
        if type(group) is int:
            return self.__candidate_list[group]["score"]
        score = 0
        for i in range(len(group)):
            score += self.__candidate_list[group[i]]["score"]
            for j in range(i + 1, len(group)):
                if self.__candidate_list[group[i]]["start_index"] <= self.__candidate_list[group[j]]["end_index"] and self.__candidate_list[group[j]]["start_index"] <= self.__candidate_list[group[i]]["end_index"]:
                    return -1
        return score

    def __reverse_target(self):
        for group in self.__best_group:
            target_clone = copy.deepcopy(self.__targetList)
            if type(group) is int:
                solution = self.__candidate_list[group]
                self.__reverse_slice(solution["start_index"], solution["end_index"], target_clone)
            else:
                for item in group:
                    solution = self.__candidate_list[item]
                    self.__reverse_slice(solution["start_index"], solution["end_index"], target_clone)
            self.__reversed_target.append(target_clone)

    def __get_min_sort_time(self):
        results = []
        for target_list in self.__reversed_target:
            results.append(self.__bubble_sort(target_list))
        return min(results)