from graphviz import Graph

# from graphviz import Graph

# 创建一个新的 Graph 对象
dot = Graph()

# 添加节点
dot.node('A', 'Makka Pakka Land')
dot.node('B', 'MEME COIN $GUAD')
dot.node('C', 'INSCRIPTION')
dot.node('D', 'Completely based on smart contracts GameFi')

dot.node('E', 'Equipment system based on rmrk protocol')
dot.node('F', 'Contribution-based Proof of shares Recommendation system')
dot.node('G', 'Fair and open distribution method')
dot.node('H', 'Trade as brc20 on BTC network & ERC20 Token on L2(MAPO CHAIN)')
dot.node('I', 'In-game economic system')
dot.node('J', 'Rich gameplay and token consumption scenarios')

dot.node('K','Consumption of $GUAD tokens')
dot.node('M','Consumption of $MAPO tokens')
dot.node('L','Consumption of $LSGS tokens')


dot.node('O', 'MAPO-GUAD LP')
dot.node('P', 'LSGS-GUAD LP')
dot.node('X', 'GUAD-ENERGY LP')
dot.node('Y', 'GUAD-METAL LP')
dot.node('b', 'GUAD-WOOD LP')

dot.node('Q', 'Equipment system Consumption')
dot.node('R', 'Recommendation system Consumption')
dot.node('S', 'Bet system Consumption($MAPO)')
dot.node('T', 'Bet system Consumption($LSGS)')
dot.node('Y', 'BUILDING system')

# IN GAME TOKEN.

dot.node('U', 'Energy Token as every day Reward.')
dot.node('V', 'Metal tokens Obtained through the game')
dot.node('a', 'In Game Wood Token')







# 添加连接
dot.edges(['AB', 'AC', 'CG', 'CH', 'AD', 'DE','DF', 'DI', 'DJ', 'IJ','KO', 'KP', 'MO','LP',
           'QO', 'QP', 'KR', 'SM', 'TL', 'RU','UI', 'UJ', 'BO', 'BP','VQ', 'UQ', 'BX','BY',
           'UX', 'UY', 'aY', 'bY', 'Ia', 'IY'])

# 设置节点样式
dot.node('A', style='filled', color='lightblue')

# 保存并显示图像
dot.render('Makka_Pakka_Map', format='png', view=True)