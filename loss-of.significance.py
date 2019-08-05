#Mauricio Sanchez
import matplotlib.pylab as plt
def f(x):
	number = x*((4*(x**2) + 1)**0.5 + 2*x)
	return number

def g(x):
	number = x/((4*(x**2) + 1)**0.5 - 2*x)
	return number

returns = []
g_returns = []
errors = []
g_errors = []
value = -1
for i in range(12):
	r = f(value*(10**i))
	e = ((r - -0.25)/0.25)*100
	returns.append(r)
	errors.append(e)
	r_g = g(value*(10**i))
	e_g = ((r_g - -0.25)/0.25)*100
	g_returns.append(r_g)
	g_errors.append(e_g)

print("f(x):")
for i in range(len(returns) - 1):
	print('value: ' + str(returns[i]) + ' relative error: ' + str(errors[i]) + '%')	

print("g(x)")
for i in range(len(g_returns) - 1):
	print('value: ' + str(g_returns[i]) + ' relative error: ' + str(g_errors[i]) + '%')	

lista = [1,2,3,4,5,6,7,8,9,10,11,12]

plt.plot(lista,errors,label="f(x)")
plt.plot(lista,g_errors,label="g(x)")


plt.xlabel('N, where N is -1*10**N')
plt.ylabel('relative error (%)')
plt.title('Loss of significance')
plt.grid(True)

#Set the legend to be outside the ax
ax = plt.gca()
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width, 0.81*box.height])
ax.legend(loc='lower left', bbox_to_anchor=(0, 1.00))
plt.savefig("fig.png")

plt.show()