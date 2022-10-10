import hashlib

class BasicBlock:
	def __init__(self,index,transactions,previous_hash):
		self.index = index
		self.previous_hash = previous_hash
		
		self.block_data = '-'.join(transactions) + '-' + previous_hash
		self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

	def calculate_hash(self):
		return hashlib.sha256(self.block_data.encode()).hexdigest()				

class BasicChain:
	def __init__(self):
		self.blocks = []
	
	def add_block(self,block):
		self.blocks.append(block)

	def print_blocks(self):
		for item in self.blocks:
			print(f'{item.index} {item.block_data} {item.block_hash}')

	def is_chain_valid(self):
		block_list = self.blocks
		list_len = len(block_list)
		if list_len > 1:
			for i in range(1,list_len):
				c_block = block_list[i]
				p_block = block_list[i-1]

				if c_block.previous_hash != p_block.block_hash:
					return False

				if c_block.block_hash != c_block.calculate_hash():
					return False

		return True


def main():
	t1 = 'Mike sends 2BC to Jim'
	t2 = 'Jim sends 2BC to Pam'
	t3 = 'Mike sends 0.5BC to Dwight'
	t4 = 'Dwight sends 5BC to Mike'
	t5 = 'Dwight sends 2BC to Pam'
	t6 = 'Jim sends 1BC to Dwight'

	initial_block = BasicBlock(0,[t1,t2],'Initial block')
	first_block = BasicBlock(1,[t3,t4],initial_block.block_hash)
	second_block = BasicBlock(2,[t4,t5],first_block.block_hash)

	basic_chain = BasicChain()
	basic_chain.add_block(initial_block)
	basic_chain.add_block(first_block)
	basic_chain.add_block(second_block)
	basic_chain.print_blocks()
	check = basic_chain.is_chain_valid()
	if check == True:
		print('Chain is valid')
	else: 
		print('Chain is not valid')
	
if __name__ == '__main__':
	main()