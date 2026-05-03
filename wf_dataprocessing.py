#
# 5/2 Note:
# No scraping was needed
# This file was left blank in MS3, pre-downloaded dataset files were intended for use instead





### IGNORE SCRATCH BELOW ###
#
#
# import csv
#
# import pandas as pd
#
# def merge_datasets():
#     prob_id = list()
#     # prob_id.append(llm_set['problem_id'])
#     # prob_id.append(human_set['problem_id'])
#
#     sub_id = list()
#     # sub_id.append(llm_set['submission_id'])
#     # sub_id.append(human_set['submission_id'])
#
#     label = list()
#     # label.append(llm_set['label'])
#     # label.append(human_set['label'])
#
#     code = list()
#     # code.append(llm_set['code'])
#     # code.append(human_set['code'])
#
#     status = list()
#     # status.append(llm_set['status_in_folder'])
#     # status.append(human_set['status_in_folder'])
#
#     sizes = list()
#     ratios = list()
#
#
#
#     # next three lines reason for 2829 zeroes
#     # code_size = list()
#     # for sample in llm_set['code']:
#     #     code_size.append(code_sizer(repr(sample)))
#     # code_size.append(human_set['code_size'])
#
#     llm_set = pd.read_csv('data_original\\created_dataset_with_llms.csv')
#     human_set = pd.read_csv('data_original\\human_selected_dataset.csv')
#
#     merged = pd.concat([llm_set, human_set], join='inner', axis = 1) #ignore_index=True)
#     # llm_set.to_csv('data_processed\\merged_dataset.csv')
#
#     #merged = llm_set.merge(human_set)
#     merged.to_csv('data_processed\\merged_dataset.csv')
#
# '''
#     #append all columns values into distinct lists
#     llm_set = open('data_original\\created_dataset_with_llms.csv', mode='r', encoding='utf-8')
#     file = csv.DictReader(llm_set)
#     llm_set_length= 0
#     for entry in file:
#         prob_id.append(entry.get('problem_id'))
#         sub_id.append(entry.get('submission_id'))
#         label.append(entry.get('label'))
#         code.append(entry.get('code'))
#         sizes.append(code_sizer(repr(entry.get('code'))))
#         ratios.append(cf_ratio(repr(entry.get('code'))))
#         status.append(entry.get('status'))
#         sub_id.append(entry.get('problem_id'))
#         llm_set_length += 1
#
#     human_set = open('data_original\\human_selected_dataset.csv', mode='r', encoding='utf-8')
#     file = csv.DictReader(human_set)
#     human_set_length= 0
#     for entry in file:
#         prob_id.append(entry.get('problem_id'))
#         sub_id.append(entry.get('submission_id'))
#         label.append(entry.get('label'))
#         code.append(entry.get('code'))
#         sizes.append(code_sizer(repr(entry.get('code'))))
#         ratios.append(cf_ratio(repr(entry.get('code'))))
#         status.append(entry.get('status'))
#         sub_id.append(entry.get('problem_id'))
#         human_set_length += 1
#
#
#
#     #write lists into csv file
#     outfile = open('data_processed\\merged_dataset.csv', 'w', encoding='utf-8')
#     fieldnames = ['problem_id', 'submission_id', 'label', 'code', 'code_size', 'comment_to_function_ratio', 'status_in_folder']
#     writer = csv.DictWriter(outfile, fieldnames=fieldnames)
#     #writer.writeheader()
#
# #temporary comment till line 91
#     i = 0
#     while i < (human_set_length+llm_set_length):
#         writer.writerow({'problem_id': prob_id[i],
#                          'submission_id': sub_id[i],
#                          'label': label[i],
#                          'code': code[i],
#                          'code_size': sizes[i],
#                          'comment_to_function_ratio': ratios[i],
#                          'status_in_folder': status[i]})
#         i+=1
# '''
#     # i = 0
#     # while i < (len(llm_set.index)):
#     #     sizes.append(code_sizer(repr(llm_set.loc[i, 'code'] )))
#     #     i += 1
#     #
#     # j = 0
#     # while j < (len(human_set.index)):
#     #     sizes.append(code_sizer(repr(human_set.loc[j, 'code_size'])))
#     #     j += 1
#
#
#     # i = 0
#     # while i < (len(llm_set.index)):
#     #     ratios.append(cf_ratio(repr(llm_set.loc[i, 'code'] )))
#     #
#     #     i += 1
#     #
#     # j = 0
#     # while j < (len(human_set.index)):
#     #     ratios.append(cf_ratio(repr(human_set.loc[j, 'code'] )))
#     #
#     #     j += 1
#
#
#
#     # df = pd.DataFrame(columns=['problem_id', 'submission_id', 'label', 'code', 'code_size', 'comment_to_function_ratio', 'status_in_folder'])
#     #
#     # df['problem_id'] = prob_id
#     # df['submission_id'] = sub_id
#     # df['label'] = label
#     # df['code'] = code
#     # # df['code_size'] = sizes
#     # # df['comment_to_function_ratio'] = ratios
#     # df['status_in_folder'] = status
#
#
#     # df.to_csv('data_processed\\merged_dataset.csv', sep='\t', encoding = 'utf-8', index=False, header=True)
#     # df.to_csv('data_processed\\merged_dataset.csv')
#
#
#
#
#
#
#
# def code_sizer(code_sample):
#     # loc_counter = 0
#     # while True:
#     #     res = code_sample.find('\n')
#     #     if res != -1:
#     #         loc_counter+=1
#     #     else:
#     #         break
#
#     # return loc_counter
#     return code_sample.count('\n')
#
# def cf_ratio(code_sample):
#     numerator = code_sample.count('#')
#     denominator = code_sample.count('def ')
#
#     ratio = f'{numerator}:{denominator}'
#
#     return ratio
#
#
#
#
# if __name__ == '__main__':
#     merge_datasets()
