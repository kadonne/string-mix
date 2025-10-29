def mix(s1, s2):
	freq_s1 = {i : s1.count(i) for i in set(s1)}
	freq_s2 = {i : s2.count(i) for i in set(s2)}
	temp = {}
	for i in freq_s1.keys():
		temp[i] = 0
	for i in temp:
		if freq_s1[i] == 1 or not i.isalpha() or i.isupper():
			del freq_s1[i]
	temp = {}
	for i in freq_s2.keys():
		temp[i] = 0
	for i in temp:
		if freq_s2[i] == 1 or not i.isalpha() or i.isupper():
			del freq_s2[i]
	result = {}
	for item in freq_s1:
		repeat = 0
		sign = ''
		if(freq_s2.get(item)==None or freq_s1[item] > freq_s2[item]):
			repeat = freq_s1[item]
			sign = '1'
		elif(freq_s1[item] < freq_s2[item]):
			repeat = freq_s2[item]
			sign = '2'
		elif(freq_s1[item] == freq_s2[item]):
			repeat = freq_s1[item]
			sign = '='
		repeat_key = ''
		for i in range(0,repeat):
			repeat_key = repeat_key + item
		result[repeat_key] = sign

	for item in freq_s2:
		repeat = 0
		sign = ''
		if(freq_s1.get(item)==None or freq_s1[item] < freq_s2[item]):
			repeat = freq_s2[item]
			sign = '2'
		elif(freq_s1[item] > freq_s2[item]):
			repeat = freq_s1[item]
			sign = '1'
		elif(freq_s1[item] == freq_s2[item]):
			repeat = freq_s2[item]
			sign = '='
		repeat_key = ''
		for i in range(0,repeat):
			repeat_key = repeat_key + item
		result[repeat_key] = sign
	
	maximum=0
	for item in result:
		if(len(item) > maximum):
			maximum = len(item)

	sorted_result = {}
	symbols = ['2','=']
	temp_arr = []
	while maximum >= 2:
		counter = 0
		for item in result:
			if len(item) == maximum:
				temp_arr.append(item)
		sorted_temp_arr = sorted(temp_arr)
		sorted_temp_arr_temp = sorted(temp_arr)

		while counter <= 1:
			for ele in sorted_temp_arr:
				if result[ele] == symbols[counter]:
					sorted_temp_arr_temp.append(sorted_temp_arr_temp.pop(sorted_temp_arr_temp.index(ele)))
			counter = counter +1

		sorted_temp_arr = sorted_temp_arr_temp

		for ele in sorted_temp_arr:
			sorted_result[ele] = None
		maximum = maximum -1
		temp_arr = []
		
	for i in sorted_result:
		sorted_result[i] = result[i]

	output=''
	for i in sorted_result:
		output = output + '%s:%s/'%(sorted_result[i], i)
	output = output[:-1]
	return output
