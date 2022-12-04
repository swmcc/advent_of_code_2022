#!/usr/bin/env ruby
# frozen_string_literal: true

CONTENTS = File.readlines('input.txt', chomp: true).freeze
PRIORITY = (('a'..'z').to_a + ('A'..'Z').to_a).freeze

def first_puzzle
  priorities = CONTENTS.map do |bag|
    first, second = bag.chars.each_slice((bag.size / 2).round).to_a
    items = (first & second).uniq

    items.map { |item| PRIORITY.find_index(item) + 1 }.sum
  end
  priorities.sum
end

def second_puzzle
  priorities = 0
  CONTENTS.each_slice(3) do |bags|
    first, second, third = bags
    items = (first.chars & second.chars & third.chars).uniq

    priorities += items.map { |item| PRIORITY.find_index(item) + 1 }.sum
  end
  priorities
end

puts "The answer for the first puzzle: #{first_puzzle}"
puts "The answer for the second puzzle: #{second_puzzle}"
